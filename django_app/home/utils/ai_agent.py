from groq import Groq
from .prompts import system_prompt
key = "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"

def analyze_code_with_llm(file_content,file_name):
    prompt = f"""   
             Analyze the following code for:
             - Code style and formating issues
             - potenial bugs or errors
             - performance improvements
             - best practices
            
             File : {file_name}
             Content : {file_content}         
             
             Provide a detailed JSON output with the structure
             {{
              "issue" : [
                  {{
                       "type" : "<style|bugs|performance|best_practice>",
                       "line" : <line_number>,
                       "description" : "<description>",
                       "suggestion"  : "<suggestion>
                  }}
              ]
             }}

              ```json
              
             """

    client = Groq(
                  api_key=key
            )    

    completion = client.chat.completions.create(
          model= "llama3-groq-70b-8192-tool-use-preview",
          messages=[
              {"role" : "system" , "content" : system_prompt},
              {
                  "role" : "user",
                  "content" : prompt
              }
          ],
          temperature = 0.5,
          top_p=1
     )

    return completion.choices[0].message.content