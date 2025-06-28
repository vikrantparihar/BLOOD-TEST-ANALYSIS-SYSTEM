# 📊 Blood Test Analysis System using CrewAI

This project uses [CrewAI](https://docs.crewai.com) and FastAPI to analyze blood test PDF reports and generate medical summaries using autonomous agents.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

---

## ✅ Features
- Upload a PDF blood test report.
- Extract test metrics using LLM-powered agents.
- Get a human-friendly diagnostic summary via API.

---

## 🐛 Bugs Fixed
| File         | Issue                                                                 | Fix                                                                 |
|--------------|-----------------------------------------------------------------------|---------------------------------------------------------------------|
| `main.py`    | Improper `File(.)`, hardcoded paths, broken tool/task linkage        | Corrected file handling, dynamic task tool injection                |
| `agents.py`  | `llm = llm` undefined error                                           | Defined `llm` via `ChatOpenAI` and properly instantiated agents     |
| `task.py`    | Placeholder/joke task descriptions                                    | Rewritten with safe, realistic clinical goals                       |
| `tools.py`   | Missing import `PDFLoader`, method logic incomplete                   | Replaced with `PyPDFLoader`, implemented `_run` for full PDF text   |

---

## 🚀 Setup Instructions
```bash
# 1. Clone the repository
$ git clone <your-repo-url>
$ cd crewai-blood-analysis

# 2. Create a virtual environment (optional but recommended)
$ python -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
$ pip install -r requirements.txt

# 4. Start the server
$ uvicorn main:app --reload
```

---

## 📬 API Usage
### Endpoint
```
POST /analyze
```
### Request (multipart/form-data)
- `file`: PDF file upload (e.g., blood test report)

### Response
```json
{
  "summary": "Patient's hemoglobin is within range... LDL is slightly elevated..."
}
```

---

## ⚙️ CrewAI Agents
| Role               | Description                                                |
|--------------------|------------------------------------------------------------|
| PDF Analyst        | Extracts raw test data from PDF                            |
| Medical Diagnostician | Evaluates the data and identifies abnormalities         |
| Report Writer      | Creates a readable diagnostic summary                      |

---

## 🧪 Example Command (using `curl`)
```bash
curl -X POST "http://localhost:8000/analyze" \
  -H  "accept: application/json" \
  -H  "Content-Type: multipart/form-data" \
  -F "file=@blood_test_report.pdf"
```

---

## 🎯 Bonus Upgrade Roadmap (Optional)

### 1. 🧵 Celery + Redis (Concurrent Task Queue)
- Use Celery workers to offload PDF processing jobs.
- Add Redis as the message broker.
- Ensures non-blocking performance for multiple uploads.

### 2. 🗃️ Database Integration (User/Report History)
- Store uploaded PDFs and results in PostgreSQL or SQLite.
- Track user sessions or metadata.
- Provide admin dashboard to view reports.

---

## 📊 Tech Stack
- Python 3.10+
- FastAPI
- CrewAI
- LangChain
- OpenAI (ChatOpenAI)
- PyPDFLoader
- Uvicorn

---

## ✨ Future Ideas
- Add authentication layer (JWT)
- Visual report generation (charts)
- Email report delivery

---

## ✉️ License
MIT License

---

Built with ❤️ by your AI Assistant.
