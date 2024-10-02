import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"),)
completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {
            "role": "user",
            "content": "Write an email to my boss for resignation"
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)

print(completion)


'''

ChatCompletion(id='chatcmpl-b8a9005c-a3cb-49ee-a1d5-b026c84621e7', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content="Here is a sample email you can use as a template:\n\nSubject: 
Notification of Resignation\n\nDear [Boss's Name],\n\nI am writing to inform you that I have decided to resign from my position as [Position] at [Company Name], effective [Date of Last Day of Work].\n\nI am grateful for the opportunities I have had while working at [Company Name], and I appreciate the experience and skills I have gained during my time here. However, I have decided that it is time for me to move on and explore new opportunities.\n\nI will do my best to ensure a smooth transition of my responsibilities and complete any outstanding tasks before my departure. If there is anything specific you would like me to focus on during my remaining time here, please let me know.\n\nThank you again for the opportunity to work at [Company Name]. I wish the company all the best for the future.\n\nSincerely,\n\n[Your Name]\n\nPlease note that you should customize this template to fit your specific situation and circumstances. You may also want to include additional information, such as:\n\n* A specific reason for your resignation (optional)\n* A lengthier explanation of your accomplishments and contributions during your time at the company\n* An offer to assist with the transition and training of a replacement\n* A mention of any outstanding vacation time or benefits you are entitled to\n\nRemember to keep the tone professional and respectful, regardless of the reason for your resignation.", role='assistant', function_call=None, tool_calls=None))], created=1727848003, model='llama3-8b-8192', object='chat.completion', system_fingerprint='fp_a97cfe35ae', usage=CompletionUsage(completion_tokens=287, prompt_tokens=18, total_tokens=305, completion_time=0.239166667, prompt_time=0.005849775, queue_time=0.029535048, total_time=0.245016442), x_groq={'id': 'req_01j95w8dtgfn5vqt01gkcfzf2x'})

'''
