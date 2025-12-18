import streamlit as st
import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.rag.rag_engine import AssessmentRecommendationEngine

st.title("🧠 SHL GenAI Assessment Recommendation")

query = st.text_area("Enter Job Description")

import pandas as pd
import plotly.express as px

@st.cache_resource
def get_engine():
    return AssessmentRecommendationEngine()

if st.button("Recommend"):
    try:
        engine = get_engine()
        
        # Get recommendations directly from the engine
        explanation = engine.recommend(query)
        docs = engine.search(query, k=10)
        
        results = []
        for doc in docs:
            meta = doc.metadata
            test_type = meta.get("test_type", "")
            if isinstance(test_type, str):
                test_type = test_type.split(",")
                
            results.append({
                "url": meta.get("url", ""),
                "name": meta.get("name", ""),
                "description": meta.get("description", ""),
                "test_type": test_type,
                "duration": meta.get("duration", 0),
                "remote_support": meta.get("remote_support", "Yes"),
                "adaptive_support": meta.get("adaptive_support", "No")
            })
            
        res = {
            "recommended_assessments": results,
            "explanation": explanation
        }

        st.subheader("Recommended Assessments")
        
        # Collect data for visualization
        all_test_types = []

        for i, r in enumerate(res["recommended_assessments"], 1):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                # Title with Link
                st.markdown(f"### {i}. [{r['name']}]({r['url']})")
                
                # Test Type
                test_types = r['test_type']
                if isinstance(test_types, list):
                    test_types_str = ", ".join(test_types)
                    all_test_types.extend(test_types)
                else:
                    test_types_str = str(test_types)
                    all_test_types.append(test_types_str)
                    
                st.markdown(f"**Test Type:** {test_types_str}")
                
                # Description / Relevance
                # Using description as relevance context for now
                st.markdown(f"**Description:** {r['description']}")

            with col2:
                st.markdown(f"**Remote Testing:** {r.get('remote_support', 'N/A')}")
                st.markdown(f"**Adaptive/IRT:** {r.get('adaptive_support', 'N/A')}")
                
                duration = r.get('duration', 0)
                duration_str = f"{duration} minutes" if duration else "N/A"
                st.markdown(f"**Duration:** {duration_str}")

            st.markdown("---")

        # Visualization Section
        st.subheader("Visualization of Test Types")
        if all_test_types:
            # Clean up whitespace
            all_test_types = [t.strip() for t in all_test_types if t.strip()]
            type_counts = pd.Series(all_test_types).value_counts().reset_index()
            type_counts.columns = ["Test Type", "Count"]
            
            fig = px.bar(type_counts, x="Test Type", y="Count", title="Distribution of Test Types Recommendations")
            st.plotly_chart(fig)

        st.subheader("AI Explanation")
        st.write(res["explanation"])
        
    except requests.exceptions.JSONDecodeError:
        st.error("Error: Invalid JSON response from server.")
        st.text(f"Status Code: {response.status_code}")
        st.text(f"Raw Response: {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
