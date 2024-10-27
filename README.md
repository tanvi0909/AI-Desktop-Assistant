# AI Desktop Assistant

An AI-powered desktop assistant built using the LLaMA model and Groq API, designed for voice-based interactions. This assistant can answer questions conversationally, perform specific tasks (like opening websites, playing music, or fetching news and weather updates), and follow specific voice commands to save responses or quit operations.

## Features

<img align="right" alt="ai" src="https://github.com/tanvi0909/assets/blob/main/ai-desktop-assistant.avif" width="300"  />

- **Conversational AI**: Uses the LLaMA model with Groq API to interact with the user in a conversational style.
- **Voice Recognition & Output**: Takes voice input from the user and provides spoken responses.
- **Task Automation**:
  - **Time Inquiry**: Provides the current time upon request.
  - **Website Navigation**: Opens specific websites like Google, YouTube, etc., on voice command.
  - **Music Player**: Plays songs from the local folder by recognizing song names in the command.
  - **News and Weather Updates**: Fetches live updates using news and weather APIs.
  - **Answer Saving**: Saves answers to questions in a file when specified by the user.
  
## Specific Commands & Instructions

The assistant responds to the following commands in a precise way:
- **Answer Saving**: Say “using artificial intelligence” in your query for the assistant to save its response to a file.
- **News & Weather Updates**: Mention “news” or “weather” in your query for respective updates.
- **Music**: Use the command "play [songname]" to play a specific song from the local folder.
- **Open Websites**: Say “open [sitename]” (e.g., “open YouTube”) to navigate to that site.
- **Exit Command**: Say “Jarvis quit” to close the assistant.

## How to Run

1. **Install Requirements**: Ensure all dependencies (e.g., speech recognition libraries, APIs) are installed.
2. **Set API Keys**:
   - **Groq API Key**: Required for conversational interactions.
   - **News API & Weather API Keys**: Required for fetching live updates.
3. **Run the Assistant**: Run the main.py file and interact using your voice for a hands-free experience.

## File Structure

- `main.py`: Core file to initiate the assistant.
- `requirements.txt`: List of dependencies to be installed.
- `responses/`: Directory where saved answers are stored.
- `music/`: Local folder containing playable songs.

## Future Improvements

- **Enhanced Command Recognition**: Additional commands and task automation.
- **Customizable Responses**: Option to customize responses based on user preferences.

## Example Commands

| Command                        | Action Performed                        |
|--------------------------------|-----------------------------------------|
| "What is the time?"            | Provides the current time.              |
| "Open YouTube"                 | Opens YouTube in the default browser.   |
| "Play [songname]"              | Plays specified song from local music.  |
| "Give me the news"             | Fetches current news updates.           |
| "Using artificial intelligence, tell me..." | Saves the answer to a file. |
| "Jarvis Quit"                         | Closes the assistant.                   |

