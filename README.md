<div align="center">

# 🧠 LLM Quiz App - Ollama Based

### *AI-Powered Coding Challenge Generator*

[![Python](https://img.shields.io/badge/Python-3.13+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![React](https://img.shields.io/badge/React-19-61dafb?style=for-the-badge&logo=react&logoColor=black)](https://reactjs.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Ollama](https://img.shields.io/badge/Ollama-AI-000000?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.ai)

*Generate unlimited coding challenges with the power of local AI models*

[🚀 Quick Start](#-quick-start) • [📖 Documentation](#-features) • [🛠️ Tech Stack](#-tech-stack) • [🤝 Contributing](#-contributing)

</div>

---

## 🌟 Features

<table>
<tr>
<td width="50%">

### 🤖 **AI-Powered Generation**
- Generate coding challenges using local Ollama models
- Support for multiple programming languages
- Adaptive difficulty levels (Easy, Medium, Hard)
- Smart question validation and formatting

### 🔐 **Secure Authentication**
- Seamless user authentication with Clerk
- Protected routes and user sessions
- Automatic user management

</td>
<td width="50%">

### 📊 **Smart Quota System**
- Daily challenge generation limits
- Automatic quota reset every 24 hours
- Fair usage monitoring
- Real-time quota tracking

### 🎨 **Modern User Experience**
- Beautiful, responsive design
- Smooth animations and transitions
- Glass morphism effects
- Mobile-first approach

</td>
</tr>
</table>

### ✨ **Additional Features**
- 📚 **Challenge History** - Track all your completed challenges
- ⚡ **Lightning Fast** - Local AI processing with no external API calls
- 🔄 **Multiple Models** - Support for various Ollama models
- 📱 **Cross-Platform** - Works on desktop and mobile devices

---

## 🎬 **Demo**

<div align="center">

### 🖼️ Screenshots

| Challenge Generation | User Dashboard | Challenge History |
|:---:|:---:|:---:|
| ![Challenge](https://via.placeholder.com/300x200/3b82f6/ffffff?text=Challenge+Generation) | ![Dashboard](https://via.placeholder.com/300x200/8b5cf6/ffffff?text=User+Dashboard) | ![History](https://via.placeholder.com/300x200/10b981/ffffff?text=Challenge+History) |

*Beautiful, modern interface with smooth animations*

</div>

---

## 🛠️ **Tech Stack**

<div align="center">

### Frontend
![React](https://img.shields.io/badge/React-19-61dafb?style=flat-square&logo=react&logoColor=black)
![Vite](https://img.shields.io/badge/Vite-Latest-646cff?style=flat-square&logo=vite&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Modern-1572b6?style=flat-square&logo=css3&logoColor=white)
![React Router](https://img.shields.io/badge/React_Router-6-ca4245?style=flat-square&logo=react-router&logoColor=white)

### Backend
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-009688?style=flat-square&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-d71f00?style=flat-square&logo=sqlite&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-V2-e92063?style=flat-square&logo=pydantic&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003b57?style=flat-square&logo=sqlite&logoColor=white)

### AI & Authentication
![Ollama](https://img.shields.io/badge/Ollama-Local_AI-000000?style=flat-square&logo=ollama&logoColor=white)
![Clerk](https://img.shields.io/badge/Clerk-Auth-6c47ff?style=flat-square&logo=clerk&logoColor=white)

</div>

---

## 🚀 **Quick Start**

### 📋 **Prerequisites**

Before you begin, ensure you have the following installed:

```bash
# Check your versions
node --version  # v16.0.0 or higher
python --version  # 3.13.0 or higher
ollama --version  # Latest version
```

<details>
<summary>📥 <strong>Installation Links</strong></summary>

- **Node.js**: [Download from nodejs.org](https://nodejs.org/)
- **Python**: [Download from python.org](https://python.org/)
- **Ollama**: [Download from ollama.ai](https://ollama.ai/)

</details>

### 🔧 **Installation**

#### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/HarshithMandi/LLMquizapp-OllamaBased.git
cd LLMquizapp-OllamaBased
```

#### 2️⃣ **Setup Backend**
```bash
cd backend
pip install -e .
```

#### 3️⃣ **Setup Frontend**
```bash
cd ../frontend
npm install
```

#### 4️⃣ **Install AI Models**
```bash
# Recommended: Fast and efficient
ollama pull qwen2.5-coder:7b

# Alternative options:
ollama pull codellama:7b
ollama pull llama3.2:8b
```

#### 5️⃣ **Environment Configuration**

<details>
<summary>🔐 <strong>Backend Environment (.env)</strong></summary>

Create `backend/.env`:
```env
# Clerk Authentication
CLERK_SECRET_KEY=your_clerk_secret_key
CLERK_PUBLISHABLE_KEY=your_clerk_publishable_key

# Ollama Configuration
OLLAMA_URL=http://localhost:11434/api/generate
OLLAMA_MODEL=qwen2.5-coder:7b

# Database
DATABASE_URL=sqlite:///./database.db
```

</details>

<details>
<summary>🔐 <strong>Frontend Environment (.env)</strong></summary>

Create `frontend/.env`:
```env
VITE_CLERK_PUBLISHABLE_KEY=your_clerk_publishable_key
```

</details>

### 🎯 **Running the Application**

#### Terminal 1: Start Ollama
```bash
ollama serve
```

#### Terminal 2: Start Backend
```bash
cd backend
python server.py
```

#### Terminal 3: Start Frontend
```bash
cd frontend
npm run dev
```

🎉 **Visit [http://localhost:5173](http://localhost:5173) to start generating challenges!**

---

## 🎮 **Usage Guide**

### 🔐 **Getting Started**
1. **Sign Up/Login** - Create an account or sign in with Clerk
2. **Choose Difficulty** - Select Easy, Medium, or Hard
3. **Generate Challenge** - Click the generate button
4. **Answer Questions** - Select your answer from multiple choices
5. **View Explanation** - Learn from detailed explanations
6. **Track Progress** - Check your history and remaining quota

### 🎛️ **Configuration Options**

<details>
<summary>🤖 <strong>AI Model Configuration</strong></summary>

You can switch between different Ollama models by updating your `.env`:

```env
# For speed (recommended)
OLLAMA_MODEL=qwen2.5-coder:7b

# For coding focus
OLLAMA_MODEL=codellama:7b

# For general knowledge
OLLAMA_MODEL=llama3.2:8b
```

</details>

<details>
<summary>📊 <strong>Quota Management</strong></summary>

Modify daily limits in `backend/src/database/models.py`:

```python
quota_remaining = Column(Integer, nullable=False, default=10)  # Change default value
```

</details>

---

## 🏗️ **Project Structure**

```
LLMquizapp-OllamaBased/
├── 📁 frontend/                 # React application
│   ├── 📁 src/
│   │   ├── 📁 auth/            # Authentication components
│   │   ├── 📁 challenge/       # Challenge generation
│   │   ├── 📁 history/         # History management
│   │   └── 📁 layout/          # Layout components
│   ├── 📄 package.json
│   └── 📄 vite.config.js
│
├── 📁 backend/                  # FastAPI application
│   ├── 📁 src/
│   │   ├── 📁 database/        # Database models & operations
│   │   ├── 📁 routes/          # API endpoints
│   │   ├── 📄 ai_generator.py  # AI integration
│   │   └── 📄 utils.py         # Utility functions
│   ├── 📄 pyproject.toml
│   └── 📄 server.py
│
├── 📄 README.md
├── 📄 .gitignore
└── 📄 LICENSE
```

---

## 🔧 **API Documentation**

### 🚀 **Endpoints**

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/challenge/generate-challenge` | Generate a new challenge |
| `GET` | `/api/challenge/quota` | Get user's remaining quota |
| `GET` | `/api/challenge/my-history` | Fetch user's challenge history |

### 📝 **Example Request**

```bash
curl -X POST "http://localhost:8000/api/challenge/generate-challenge" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_clerk_token" \
  -d '{"difficulty": "medium"}'
```

---

## 🎨 **Customization**

### 🎭 **Styling**

The app uses a modern CSS design system with:
- **CSS Variables** for consistent theming
- **Animations** with CSS keyframes
- **Glass Morphism** effects
- **Responsive Design** for all devices

### 🎨 **Color Customization**

Modify colors in `frontend/src/index.css`:

```css
:root {
  --primary-500: #3b82f6;    /* Change primary color */
  --success-500: #22c55e;    /* Change success color */
  --error-500: #ef4444;      /* Change error color */
}
```

---

## 🤝 **Contributing**

We welcome contributions! Here's how you can help:

### 🐛 **Bug Reports**
- Use the issue tracker
- Include steps to reproduce
- Provide system information

### 💡 **Feature Requests**
- Describe the feature
- Explain the use case
- Provide mockups if possible

### 🔄 **Pull Requests**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 **Acknowledgments**

- **[Ollama](https://ollama.ai/)** - For making local AI accessible
- **[Clerk](https://clerk.dev/)** - For seamless authentication
- **[FastAPI](https://fastapi.tiangolo.com/)** - For the amazing Python framework
- **[React](https://reactjs.org/)** - For the powerful frontend library

---

<div align="center">

### 🌟 **Star this repository if you found it helpful!**

Made with ❤️ by [HarshithMandi](https://github.com/HarshithMandi)

[⬆ Back to Top](#-llm-quiz-app---ollama-based)

</div>
````

This README includes:

## ✨ **Key Features:**
- **Visual Appeal** with badges, emojis, and structured layout
- **Comprehensive Setup** with step-by-step instructions
- **Screenshots placeholder** section for demo images
- **Detailed Tech Stack** with technology badges
- **API Documentation** with example requests
- **Customization Guide** for styling and configuration
- **Contributing Guidelines** for open source collaboration
- **Professional Structure** with clear sections

## 🎯 **Improvements Made:**
1. **Better Visual Hierarchy** with emojis and badges
2. **Collapsible Sections** for detailed information
3. **Code Examples** with syntax highlighting
4. **Table Layouts** for better organization
5. **Interactive Elements** with links and navigation
6. **Professional Formatting** with consistent styling

