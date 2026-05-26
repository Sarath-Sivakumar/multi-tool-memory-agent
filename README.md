## 🚀 Features

* 🧠 **Short-Term Conversational Memory**: Retains context, user details, and dialogue history during the active session to enable fluid and relevant multi-turn conversations.
* 🌦️ **Real Weather Integration**: Hooks directly into a live weather service API to fetch accurate, localized atmospheric data on demand.
* 🛠️ **Dynamic Tool Calling**: Autonomously determines when the user is asking about the weather, extracts location variables, and executes the weather tool seamlessly.

---

## 📁 Project Structure

```text
multi-tool-memory-agent/
│
├── agent/                  # Core orchestration logic
│   ├── __init__.py
│   └── orchestrator.py     # Main agent reasoning loop and history tracking
│
├── tools/                  # External integrations and APIs
│   ├── __init__.py
│   └── weather.py          # Real weather API tool implementation
│
├── memory/                 # Session state management
│   ├── __init__.py
│   └── short_term.py       # Conversational memory buffer
│
├── .env.example            # Configuration template for credentials
├── requirements.txt        # Project dependencies
├── main.py                 # Application entry point
└── README.md
