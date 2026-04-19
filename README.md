<<<<<<< HEAD
# CHATBOTX Course Advisor Chatbot
=======
#  Course Advisor Chatbot
>>>>>>> 50474ff9b34f821d6d0f60ce857f82bea810854e

A multi-interface chatbot application designed to help prospective students with course inquiries. The chatbot provides information about courses, fees, syllabus, batch schedules, and enrollment processes using the GROQ API with the Llama 3.3 model.

---

## Features

- **Multi-Interface Support**: Access the chatbot via Streamlit web UI, terminal CLI, or Flask REST API
- **Real-time Streaming**: Stream responses from the AI model for better user experience
- **Session Management**: Maintain conversation history across multiple interactions
- **Comprehensive Course Information**: Detailed data on offered courses including fees, duration, syllabus, and EMI options
- **Quick Questions**: Predefined quick questions for common inquiries
- **Error Handling**: Robust error handling and user-friendly error messages

---

## Project Structure

```
CHATBOTX/
├── app.py              # Streamlit web UI application
├── bot.py              # Core chatbot logic with prompt detection
├── chatbot.py          # Command-line interface (CLI)
├── server.py           # Flask REST API server with HTML UI
├── config.py           # Central configuration management
├── prompts.py          # Multiple system prompts for different contexts
├── index.html          # Modern web interface (CSS + JavaScript)
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- GROQ API key (from [console.groq.com](https://console.groq.com))

### Steps

1. **Clone or download the project**:
   ```bash
   cd CHATBOTX
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the project root:
   ```env
   GROQ_API_KEY=gsk_your_api_key_here
   ```

---

## Configuration

All configuration is managed through `config.py`. Key settings include:

### API Settings
- **GROQ_API_KEY**: Your GROQ API key (loaded from `.env`)
- **MODEL**: `llama-3.3-70b-versatile` (AI model used for responses)
- **MAX_TOKENS**: `1024` (Maximum tokens per response)
- **TEMPERATURE**: `0.7` (0 = focused, 1 = creative)

### Application Settings
- **APP_TITLE**: `Course Advisor` (Application name with emoji)
- **APP_ICON**: `book` (Emoji icon for web UI)
- **APP_CAPTION**: Description of the chatbot's purpose
- **WELCOME_MESSAGE**: Initial greeting message for new conversations
- **QUICK_QUESTIONS**: List of predefined quick question suggestions

---

## Usage

### 1. Streamlit Web Interface

Provides an interactive web-based UI with:
- Real-time message streaming
- Chat message history display
- Quick question buttons in sidebar
- Conversation reset functionality
- Responsive design

**Run**:
```bash
streamlit run app.py
```

**Access**: Opens automatically in browser (typically `http://localhost:8501`)

---

### 2. Command-Line Interface (CLI)

Text-based terminal interface with:
- Interactive command processing
- Quick question suggestions
- Demo mode for testing
- Command support: `quit`, `reset`, `help`, `demo`

**Run**:
```bash
python chatbot.py
```

**Commands**:
- `quit` - Exit the chatbot
- `reset` - Start a new conversation
- `help` - Show available commands
- `demo` - Run a quick demo conversation

---

### 3. Flask REST API Server

HTTP API with built-in Web UI:
- Session-based conversation management
- JSON request/response format
- Health check endpoint
- **Modern HTML/CSS Web Interface** - Beautiful, responsive UI
- Quick questions endpoint

**Run**:
```bash
python server.py
```

**Access**:
- **Web UI**: `http://localhost:5000` - Interactive web interface with modern design
- **API Base**: `http://localhost:5000`

---

## Web Interface Features

The modern HTML/CSS web interface (`index.html`) provides an elegant user experience:

### Design Features
- **Modern Gradient UI**: Purple-to-indigo gradient theme with smooth animations
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Real-time Chat**: Instant message display with typing animations
- **Auto-scrolling**: Chat automatically scrolls to latest message
- **Message Animations**: Smooth slide-in animations for new messages

### Functionality
- **Session Management**: Auto-generates unique session IDs
- **Conversation History**: Maintains full chat history in current session
- **Reset Button**: Clear conversation and start fresh anytime
- **Send Button**: Easy message sending with visual feedback
- **Status Badge**: Shows online status in real-time
- **Typing Indicator**: Animated typing dots while waiting for response

### User Experience
- **Auto-resizing Textarea**: Input area expands as you type
- **Enter to Send**: Press Enter to send, Shift+Enter for new line
- **Helpful Placeholders**: Clear input guidance
- **Scroll Bar**: Styled scrollbar for better aesthetics
- **Focus Management**: Auto-focuses input on page load
- **Error Handling**: User-friendly error messages

### Visual Design
- Clean, modern aesthetic with professional color scheme
- Smooth transitions and hover effects
- Distinct user vs bot message styling
- Custom scrollbar styling
- Mobile-optimized layout with breakpoints
- Accessibility-friendly design

---

### GET `/`
Health check and API information
- **Response**: JSON with app info and available endpoints

### POST `/chat`
Send a message and get a response
- **Request Body**:
  ```json
  {
    "message": "What courses do you offer?",
    "session_id": "user123"
  }
  ```
- **Response**:
  ```json
  {
    "user_message": "What courses do you offer?",
    "bot_reply": "We offer three main courses...",
    "session_id": "user123"
  }
  ```

### GET `/new`
Start a new conversation
- **Query Parameters**: `session_id` (optional, defaults to 'default')
- **Response**: Confirmation with session ID

### GET `/questions`
Get list of quick questions
- **Response**:
  ```json
  {
    "questions": [
      "What courses do you offer?",
      "What is the AI/ML bootcamp fee?",
      ...
    ]
  }
  ```

---

## Courses Offered

### 1. Python Basics
- **Fee**: ₹12,000 (EMI: ₹2,000/month × 6)
- **Duration**: 2 months
- **Mode**: Fully online (live + recorded)
- **Certificate**: Yes

### 2. Data Science with Python
- **Fee**: ₹18,000 (EMI: ₹3,000/month × 6)
- **Duration**: 3 months
- **Mode**: Hybrid (online + weekend workshops)
- **Certificate**: Yes, industry-recognized

### 3. AI/ML Bootcamp
- **Fee**: ₹25,000 (EMI: ₹4,200/month × 6)
- **Duration**: 3 months
- **Mode**: Fully online (Mon-Fri 7-9 PM IST)
- **Placement**: Yes (resume prep, mock interviews)
- **Certificate**: Yes, with LinkedIn badge

---

## Batch Information

- **Next Batch Start**: 1 July 2026
- **Batch End**: 31 December 2026
- **Registration Deadline**: 20 June 2026
- **Registration Fee**: ₹999 (adjustable toward course fee)

---

## Enrollment

- **Website**: chatbotx.com/enroll
- **Email**: admissions@chatbotx.com
- **Phone**: 1800-XXX-XXXX (Mon-Sat, 10 AM - 6 PM IST)

---

## Core Modules

### `bot.py`
Core chatbot logic with GROQ API integration and intelligent prompt selection
- `detect_prompt_type(user_message)`: Analyzes message and selects appropriate prompt
- `chat(history, user_message)`: Non-streaming chat response with smart prompt selection
- `stream_chat(history, user_message)`: Streaming chat responses with smart prompt selection
- `new_conversation()`: Initialize empty conversation history

### `config.py`
Centralized configuration management
- API credentials and model settings
- Application display settings
- Course information and quick questions

### `prompts.py`
Multiple system prompts for different contexts
- **SYSTEM_PROMPT**: Course advisor for general inquiries
- **TECHNICAL_SUPPORT_PROMPT**: Technical troubleshooting and platform issues
- **FAQ_PROMPT**: Frequently asked questions with quick answers
- **PLACEMENT_ASSISTANT_PROMPT**: Career guidance and job placement support
- **CAREER_ADVISOR_PROMPT**: Career path recommendations based on goals
- **Smart Prompt Detection**: Automatically selects appropriate prompt based on user query

### `app.py`
Streamlit web interface
- Page configuration and session state management
- Message rendering and history display
- Chat input handling with real-time streaming
- Sidebar with quick questions and clear conversation button

### `chatbot.py`
Command-line interface
- Terminal-based chat interaction
- Command processing (quit, reset, help, demo)
- Help and demo functionality

### `server.py`
Flask REST API server
- HTTP endpoints for chatbot access
- Session-based conversation management
- JSON request/response handling
- Error handling and validation

---

## Dependencies

- **groq**: GROQ API client for LLM access
- **python-dotenv**: Environment variable management
- **streamlit**: Web UI framework
- **flask**: REST API framework

See `requirements.txt` for specific versions.

---

## Troubleshooting

### GROQ_API_KEY Error
- Ensure `.env` file exists in project root
- Verify API key is correct from [console.groq.com](https://console.groq.com)
- Check that `.env` is not in `.gitignore` (for local use only)

### Port Already in Use
- **Streamlit (8501)**: Run `streamlit run app.py --server.port 8502`
- **Flask (5000)**: Modify `port=5000` in `server.py`

### API Rate Limiting
- GROQ API has rate limits; monitor response times
- Adjust `MAX_TOKENS` in `config.py` if needed

### Empty Responses
- Verify `SYSTEM_PROMPT` in `prompts.py` is not empty
- Check GROQ API status and quota

---

## Architecture

The application follows a modular architecture:

```
User Input
    ↓
Interface Layer (app.py / chatbot.py / server.py)
    ↓
Bot Logic (bot.py)
    ↓
GROQ API
    ↓
Llama 3.3 Model
    ↓
Response
```

**Conversation Flow**:
1. User sends message
2. Message appended to history
3. History + system prompt sent to GROQ API
4. AI generates response using Llama 3.3 model
5. Response streamed or returned to user
6. Response appended to history for context

---

## Future Enhancements

- Database integration for conversation persistence
- User authentication and profiles
- Advanced analytics and feedback collection
- Multi-language support
- Document upload for course details
- Integration with enrollment system
- Admin dashboard

---

## License

Propriatary - CHATBOTX 2026

---

## Support

For technical support or inquiries:
- Email: admissions@chatbotx.com
- Phone: 1800-XXX-XXXX (Mon-Sat, 10 AM - 6 PM IST)
- Website: chatbotx.com

---

**Built with Claude AI · CHATBOTX 2026**
