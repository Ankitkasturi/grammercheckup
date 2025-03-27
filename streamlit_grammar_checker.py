import streamlit as st
import language_tool_python

def check_grammar(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    
    corrections = []
    for match in matches:
        correction = {
            'error': match.context,
            'message': match.message,
            'suggestions': match.replacements,
            'position': (match.offset, match.offset + match.errorLength)
        }
        corrections.append(correction)
    
    return corrections

def main():
    st.title("Grammar Checker")
    st.write("Enter your text below to check for grammar errors:")
    
    # Text input area
    user_text = st.text_area("", height=200)
    
    if st.button("Check Grammar"):
        if user_text.strip():
            corrections = check_grammar(user_text)
            
            if not corrections:
                st.success("No grammar errors found!")
            else:
                st.warning(f"Found {len(corrections)} potential issues:")
                
                for i, correction in enumerate(corrections, 1):
                    with st.expander(f"Issue #{i}"):
                        st.write(f"**Context:** {correction['error']}")
                        st.write(f"**Message:** {correction['message']}")
                        if correction['suggestions']:
                            st.write(f"**Suggestions:** {', '.join(correction['suggestions'])}")
        else:
            st.error("Please enter some text to check.")

    st.markdown("---")
    st.markdown("Made with ❤️ using Streamlit and LanguageTool")

if __name__ == "__main__":
    main()