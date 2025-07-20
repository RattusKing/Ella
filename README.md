# Ella
Fitness and wellness companion


```markdown
# Ella — Offline-First Wellness Chatbot

Ella is a purpose-built AI chatbot designed to serve as a personal fitness and mental well-being companion. She operates offline-first, equipped with embedded wellness knowledge and advanced conversational reasoning. Ella’s architecture balances ethical awareness, emotional intelligence, and user-centered design to offer guidance that feels both honest and supportive.

---

## Key Features

- **Offline-First Design:** Runs locally with lightweight language models and embedded knowledge to ensure privacy, low latency, and accessibility without internet.
- **Embedded Wellness Knowledge:** Includes curated fitness, nutrition, and mental health advice tailored to individual goals.
- **Ethically Guided Reasoning:** Implements a moral engine inspired by Stoic philosophy and Buddhist mindfulness for wise, balanced recommendations.
- **Simulated Learning:** Adapts conversational style over time to feel more natural and supportive.
- **Modular Architecture:** Separates frontend, backend, and core AI logic for flexible deployment (offline, hybrid, or fully online).

---

## Technology Stack

| Component         | Technology/Library             |
|-------------------|-------------------------------|
| Frontend          | React, Vite, Tailwind CSS     |
| Backend API       | Python, FastAPI, Uvicorn       |
| Language Model    | Small LLM (placeholder for Mistral/TinyLlama/others) |
| Knowledge Storage | JSON-based embedded documents  |
| Vector Search     | Local RAG system with FAISS or equivalent (planned) |

---

## Repository Structure

```

ella-chatbot/
├── app/               # React frontend source code
├── backend/           # FastAPI backend for chat processing
├── core/              # Offline chat engine and knowledge base
├── docs/              # Documentation and design philosophy
├── public/            # Static assets (logos, icons)
├── scripts/           # Utility scripts for setup and conversion
├── README.md          # This file
├── .gitignore         # Git ignore rules
├── LICENSE            # MIT License
├── requirements.txt   # Python dependencies
└── package.json       # Frontend dependencies

````

---

## Installation & Setup

### Prerequisites

- Python 3.10+
- Node.js 18+
- Git

### Backend Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r ../requirements.txt
uvicorn main:app --reload
````

### Frontend Setup

```bash
cd app
npm install
npm run dev
```

Open [http://localhost:5173](http://localhost:5173) in your browser to interact with Ella.

---

## Usage

* Type fitness or wellness questions to get tailored advice.
* Ella’s reasoning engine will prioritize ethical, balanced recommendations.
* Offline mode supports private usage without external API calls.



## Contribution

Ella is currently in MVP stage. Contributions are welcome via pull requests or issues. Please follow the code of conduct and submit meaningful, well-documented code.



## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.



## Contact & Support

For questions, feature requests, or support, please open an issue on GitHub or reach out to the maintainer.



*Ella is a work in progress and continuously improving thanks to community and user feedback.*

