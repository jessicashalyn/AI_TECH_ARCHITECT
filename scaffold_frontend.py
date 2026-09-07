import os

def create_file(path, content):
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

FILES = {
    "static/css/main.css": """
:root {
    /* Base Colors */
    --bg-dark: #0f172a;
    --bg-card: #1e293b;
    --bg-card-hover: #334155;
    --text-main: #f8fafc;
    --text-muted: #94a3b8;
    
    /* Semantic Colors */
    --color-primary: #06b6d4; /* Cyan/AI Blue */
    --color-primary-glow: rgba(6, 182, 212, 0.4);
    --color-secondary: #8b5cf6; /* Violet */
    --color-api: #14b8a6; /* Teal */
    --color-cloud: #f59e0b; /* Amber */
    --color-security: #ef4444; /* Red */
    --color-success: #10b981; /* Emerald */
    --color-border: #334155;
    
    /* Gradients */
    --gradient-primary: linear-gradient(135deg, #06b6d4, #3b82f6);
    --gradient-secondary: linear-gradient(135deg, #8b5cf6, #d946ef);
    
    /* Shadows */
    --shadow-glow: 0 0 15px var(--color-primary-glow);
    --shadow-card: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
    
    /* Transitions */
    --transition-fast: 0.2s ease;
    --transition-base: 0.3s ease;
    --transition-slow: 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    background-color: var(--bg-dark);
    color: var(--text-main);
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
    line-height: 1.6;
    overflow-x: hidden;
}

a {
    color: var(--color-primary);
    text-decoration: none;
    transition: color var(--transition-fast);
}

a:hover {
    color: #fff;
}

h1, h2, h3, h4, h5, h6 {
    font-weight: 700;
    line-height: 1.2;
    margin-bottom: 1rem;
    background-clip: text;
    -webkit-background-clip: text;
}

.text-gradient {
    background: var(--gradient-primary);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.text-gradient-secondary {
    background: var(--gradient-secondary);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.container {
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1.5rem;
}

/* Animations */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes slideUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes glowPulse {
    0% { box-shadow: 0 0 5px var(--color-primary-glow); }
    50% { box-shadow: 0 0 20px var(--color-primary-glow); }
    100% { box-shadow: 0 0 5px var(--color-primary-glow); }
}

.animate-fade-in { animation: fadeIn 1s ease forwards; }
.animate-slide-up { animation: slideUp 0.8s ease forwards; }
.delay-100 { animation-delay: 0.1s; }
.delay-200 { animation-delay: 0.2s; }
.delay-300 { animation-delay: 0.3s; }

/* Navbar */
.navbar {
    background: rgba(15, 23, 42, 0.8);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid var(--color-border);
    position: sticky;
    top: 0;
    z-index: 100;
    padding: 1rem 0;
}

.navbar .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.nav-brand {
    font-size: 1.5rem;
    font-weight: 800;
    letter-spacing: -0.5px;
}

.nav-links {
    display: flex;
    gap: 2rem;
    list-style: none;
    align-items: center;
}

.nav-link {
    color: var(--text-muted);
    font-weight: 500;
}

.nav-link:hover, .nav-link.active {
    color: var(--text-main);
}
""",
    "static/css/components.css": """
/* Buttons */
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.75rem 1.5rem;
    border-radius: 8px;
    font-weight: 600;
    cursor: pointer;
    transition: all var(--transition-base);
    border: none;
    outline: none;
    text-decoration: none;
    gap: 0.5rem;
}

.btn-primary {
    background: var(--gradient-primary);
    color: #fff;
    box-shadow: 0 4px 15px rgba(6, 182, 212, 0.3);
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(6, 182, 212, 0.5);
    color: #fff;
}

.btn-secondary {
    background: var(--bg-card);
    border: 1px solid var(--color-border);
    color: var(--text-main);
}

.btn-secondary:hover {
    background: var(--bg-card-hover);
    border-color: var(--text-muted);
    transform: translateY(-2px);
}

.btn-danger {
    background: rgba(239, 68, 68, 0.1);
    color: var(--color-security);
    border: 1px solid rgba(239, 68, 68, 0.3);
}

.btn-danger:hover {
    background: var(--color-security);
    color: #fff;
}

/* Cards */
.card {
    background: var(--bg-card);
    border-radius: 12px;
    border: 1px solid var(--color-border);
    padding: 1.5rem;
    transition: all var(--transition-base);
    box-shadow: var(--shadow-card);
}

.card:hover {
    transform: translateY(-5px);
    border-color: rgba(6, 182, 212, 0.3);
    box-shadow: 0 15px 30px -5px rgba(0,0,0,0.6), 0 0 10px rgba(6, 182, 212, 0.1);
}

/* Forms */
.form-group {
    margin-bottom: 1.5rem;
}

.form-label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 500;
    color: var(--text-muted);
}

.form-control {
    width: 100%;
    padding: 0.75rem 1rem;
    background: rgba(15, 23, 42, 0.5);
    border: 1px solid var(--color-border);
    border-radius: 8px;
    color: var(--text-main);
    font-family: inherit;
    transition: all var(--transition-fast);
}

.form-control:focus {
    outline: none;
    border-color: var(--color-primary);
    box-shadow: 0 0 0 2px rgba(6, 182, 212, 0.2);
}

select.form-control {
    appearance: none;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke='%2394a3b8'%3E%3Cpath stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M19 9l-7 7-7-7'%3E%3C/path%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: right 1rem center;
    background-size: 1rem;
}

/* Tags / Badges */
.badge {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    border-radius: 9999px;
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.badge-tech { background: rgba(6, 182, 212, 0.1); color: var(--color-primary); border: 1px solid rgba(6, 182, 212, 0.2); }
.badge-db { background: rgba(139, 92, 246, 0.1); color: var(--color-secondary); border: 1px solid rgba(139, 92, 246, 0.2); }
.badge-api { background: rgba(20, 184, 166, 0.1); color: var(--color-api); border: 1px solid rgba(20, 184, 166, 0.2); }
.badge-cloud { background: rgba(245, 158, 11, 0.1); color: var(--color-cloud); border: 1px solid rgba(245, 158, 11, 0.2); }
.badge-security { background: rgba(239, 68, 68, 0.1); color: var(--color-security); border: 1px solid rgba(239, 68, 68, 0.2); }
.badge-scale { background: rgba(16, 185, 129, 0.1); color: var(--color-success); border: 1px solid rgba(16, 185, 129, 0.2); }
""",
    "static/css/responsive.css": """
@media (max-width: 768px) {
    .nav-links {
        display: none;
    }
    
    .hero-title {
        font-size: 2.5rem;
    }
    
    .grid-2, .grid-3, .grid-4 {
        grid-template-columns: 1fr !important;
    }
}
""",
    "static/js/main.js": """
document.addEventListener('DOMContentLoaded', () => {
    // Reveal on scroll
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-slide-up');
                entry.target.style.opacity = '1';
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.reveal').forEach(el => {
        el.style.opacity = '0';
        observer.observe(el);
    });
});
""",
    "static/js/form.js": """
document.addEventListener('DOMContentLoaded', () => {
    const steps = document.querySelectorAll('.form-step');
    const nextBtns = document.querySelectorAll('.next-step');
    const prevBtns = document.querySelectorAll('.prev-step');
    const progressSteps = document.querySelectorAll('.progress-step');
    let currentStep = 0;

    function updateForm() {
        steps.forEach((step, index) => {
            step.style.display = index === currentStep ? 'block' : 'none';
            if (index === currentStep) {
                step.classList.add('animate-slide-up');
            }
        });
        
        progressSteps.forEach((progress, index) => {
            if (index < currentStep) {
                progress.classList.add('completed');
                progress.classList.remove('active');
            } else if (index === currentStep) {
                progress.classList.add('active');
                progress.classList.remove('completed');
            } else {
                progress.classList.remove('active', 'completed');
            }
        });
    }

    nextBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            if (currentStep < steps.length - 1) {
                currentStep++;
                updateForm();
            }
        });
    });

    prevBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            if (currentStep > 0) {
                currentStep--;
                updateForm();
            }
        });
    });
    
    if (steps.length > 0) {
        updateForm();
    }
    
    // Conditional logic
    const appType = document.getElementById('id_app_type');
    const aiFields = document.getElementById('conditional-ai');
    
    if (appType && aiFields) {
        appType.addEventListener('change', (e) => {
            if (e.target.value.toLowerCase().includes('ai')) {
                aiFields.style.display = 'block';
                aiFields.classList.add('animate-fade-in');
            } else {
                aiFields.style.display = 'none';
            }
        });
    }
    
    // Generate Animation
    const generateBtn = document.getElementById('generate-btn');
    const generationOverlay = document.getElementById('generation-overlay');
    const form = document.getElementById('architecture-form');
    
    if (form && generateBtn && generationOverlay) {
        form.addEventListener('submit', (e) => {
            generationOverlay.style.display = 'flex';
            
            const messages = [
                "Analyzing project requirements...",
                "Evaluating technology options...",
                "Designing database architecture...",
                "Planning API architecture...",
                "Evaluating cloud infrastructure...",
                "Running security analysis...",
                "Finalizing architecture..."
            ];
            
            const msgEl = document.getElementById('loading-message');
            let mIdx = 0;
            
            setInterval(() => {
                mIdx = (mIdx + 1) % messages.length;
                msgEl.textContent = messages[mIdx];
                msgEl.classList.remove('animate-slide-up');
                void msgEl.offsetWidth;
                msgEl.classList.add('animate-slide-up');
            }, 3000);
        });
    }
});
""",
    "static/js/dashboard.js": """
// Additional dashboard specific logic if needed
""",
    "static/js/diagrams.js": """
document.addEventListener('DOMContentLoaded', () => {
    if (typeof mermaid !== 'undefined') {
        mermaid.initialize({ 
            startOnLoad: true,
            theme: 'dark',
            themeVariables: {
                primaryColor: '#1e293b',
                primaryTextColor: '#f8fafc',
                primaryBorderColor: '#06b6d4',
                lineColor: '#94a3b8',
                secondaryColor: '#8b5cf6',
                tertiaryColor: '#14b8a6'
            },
            flowchart: { curve: 'basis' }
        });
    }
});
""",
    "templates/base.html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Tech Architect {% block title %}{% endtitle %}</title>
    
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    
    <link rel="stylesheet" href="/static/css/main.css">
    <link rel="stylesheet" href="/static/css/components.css">
    <link rel="stylesheet" href="/static/css/responsive.css">
    
    {% block extra_css %}{% endblock %}
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <a href="{% url 'home' %}" class="nav-brand text-gradient">AI Tech Architect</a>
            
            <ul class="nav-links">
                {% if user.is_authenticated %}
                    <li><a href="{% url 'projects:dashboard' %}" class="nav-link">Dashboard</a></li>
                    <li><a href="{% url 'projects:project_create' %}" class="btn btn-primary btn-sm">+ New Architecture</a></li>
                    <li>
                        <form method="post" action="{% url 'accounts:logout' %}" style="display:inline;">
                            {% csrf_token %}
                            <button type="submit" class="nav-link" style="background:none;border:none;cursor:pointer;font-family:inherit;font-size:inherit;">Logout</button>
                        </form>
                    </li>
                {% else %}
                    <li><a href="{% url 'home' %}" class="nav-link">Home</a></li>
                    <li><a href="{% url 'accounts:login' %}" class="nav-link">Login</a></li>
                    <li><a href="{% url 'accounts:register' %}" class="btn btn-primary">Register</a></li>
                {% endif %}
            </ul>
        </div>
    </nav>

    <main>
        {% block content %}{% endblock %}
    </main>

    <script src="/static/js/main.js"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
""",
    "templates/home.html": """
{% extends 'base.html' %}

{% block extra_css %}
<style>
    .hero {
        min-height: 90vh;
        display: flex;
        align-items: center;
        position: relative;
        overflow: hidden;
    }
    
    .hero-content {
        position: relative;
        z-index: 2;
        text-align: center;
        max-width: 800px;
        margin: 0 auto;
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 800;
        margin-bottom: 1.5rem;
        line-height: 1.1;
    }
    
    .hero-subtitle {
        font-size: 1.25rem;
        color: var(--text-muted);
        margin-bottom: 2.5rem;
    }
    
    .hero-actions {
        display: flex;
        gap: 1rem;
        justify-content: center;
    }
    
    /* Background Animation */
    .bg-grid {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background-size: 50px 50px;
        background-image: linear-gradient(to right, rgba(255,255,255,0.05) 1px, transparent 1px),
                          linear-gradient(to bottom, rgba(255,255,255,0.05) 1px, transparent 1px);
        transform: perspective(500px) rotateX(60deg) translateY(-100px) translateZ(-200px);
        animation: gridMove 20s linear infinite;
        z-index: 1;
        opacity: 0.3;
    }
    
    @keyframes gridMove {
        0% { transform: perspective(500px) rotateX(60deg) translateY(0) translateZ(-200px); }
        100% { transform: perspective(500px) rotateX(60deg) translateY(50px) translateZ(-200px); }
    }
    
    .glow-sphere {
        position: absolute;
        width: 300px;
        height: 300px;
        background: var(--color-primary);
        filter: blur(150px);
        opacity: 0.2;
        border-radius: 50%;
        top: 20%;
        left: 50%;
        transform: translateX(-50%);
        z-index: 1;
        animation: pulse 4s ease-in-out infinite alternate;
    }
</style>
{% endblock %}

{% block content %}
<section class="hero">
    <div class="bg-grid"></div>
    <div class="glow-sphere"></div>
    
    <div class="container hero-content animate-slide-up">
        <h1 class="hero-title"><span class="text-gradient">Design Smarter.</span><br>Architect Better.</h1>
        <p class="hero-subtitle delay-100 animate-slide-up">AI-powered technology architecture recommendations for modern applications. Instantly generate scalable, secure, and production-ready system designs.</p>
        
        <div class="hero-actions delay-200 animate-slide-up">
            {% if user.is_authenticated %}
                <a href="{% url 'projects:project_create' %}" class="btn btn-primary btn-lg">Create Architecture</a>
            {% else %}
                <a href="{% url 'accounts:register' %}" class="btn btn-primary btn-lg">Start Free</a>
                <a href="{% url 'accounts:login' %}" class="btn btn-secondary btn-lg">Login</a>
            {% endif %}
        </div>
    </div>
</section>
{% endblock %}
""",
    "templates/accounts/login.html": """
{% extends 'base.html' %}

{% block content %}
<div class="container" style="max-width: 450px; margin-top: 5rem; margin-bottom: 5rem;">
    <div class="card animate-slide-up">
        <h2 class="text-center text-gradient" style="margin-bottom: 2rem;">Welcome Back</h2>
        
        <form method="post">
            {% csrf_token %}
            {% for field in form %}
                <div class="form-group">
                    <label class="form-label">{{ field.label }}</label>
                    <input type="{{ field.field.widget.input_type }}" name="{{ field.html_name }}" class="form-control" required id="{{ field.id_for_label }}">
                    {% if field.errors %}
                        <div style="color: var(--color-security); font-size: 0.85rem; margin-top: 0.5rem;">{{ field.errors.0 }}</div>
                    {% endif %}
                </div>
            {% endfor %}
            <button type="submit" class="btn btn-primary" style="width: 100%; margin-top: 1rem;">Login</button>
        </form>
        <p class="text-center" style="margin-top: 1.5rem; color: var(--text-muted);">
            Don't have an account? <a href="{% url 'accounts:register' %}">Register here</a>
        </p>
    </div>
</div>
{% endblock %}
""",
    "templates/accounts/register.html": """
{% extends 'base.html' %}

{% block content %}
<div class="container" style="max-width: 450px; margin-top: 5rem; margin-bottom: 5rem;">
    <div class="card animate-slide-up">
        <h2 class="text-center text-gradient" style="margin-bottom: 2rem;">Create Account</h2>
        
        <form method="post">
            {% csrf_token %}
            {% for field in form %}
                <div class="form-group">
                    <label class="form-label">{{ field.label }}</label>
                    {{ field }}
                    {% if field.errors %}
                        <div style="color: var(--color-security); font-size: 0.85rem; margin-top: 0.5rem;">{{ field.errors.0 }}</div>
                    {% endif %}
                </div>
            {% endfor %}
            <button type="submit" class="btn btn-primary" style="width: 100%; margin-top: 1rem;">Register</button>
        </form>
        <p class="text-center" style="margin-top: 1.5rem; color: var(--text-muted);">
            Already have an account? <a href="{% url 'accounts:login' %}">Login here</a>
        </p>
    </div>
</div>
<script>
    document.querySelectorAll('input').forEach(i => i.classList.add('form-control'));
</script>
{% endblock %}
""",
    "templates/projects/dashboard.html": """
{% extends 'base.html' %}

{% block extra_css %}
<style>
    .dashboard-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin-bottom: 3rem;
    }
    
    .stat-card {
        padding: 2rem;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
        position: relative;
        overflow: hidden;
    }
    
    .stat-card::after {
        content: '';
        position: absolute;
        top: 0; right: 0; bottom: 0; left: 0;
        background: linear-gradient(135deg, transparent, rgba(255,255,255,0.03));
        pointer-events: none;
    }
    
    .stat-value {
        font-size: 3rem;
        font-weight: 800;
        line-height: 1;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        color: var(--text-muted);
        font-weight: 500;
    }
</style>
{% endblock %}

{% block content %}
<div class="container" style="padding-top: 3rem; padding-bottom: 5rem;">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;" class="animate-slide-up">
        <h2>Dashboard</h2>
        <a href="{% url 'projects:project_create' %}" class="btn btn-primary">+ Create New Architecture</a>
    </div>
    
    <div class="dashboard-grid animate-slide-up delay-100">
        <div class="card stat-card" style="border-top: 4px solid var(--color-primary);">
            <div class="stat-value text-gradient">{{ total_projects }}</div>
            <div class="stat-label">Total Projects</div>
        </div>
        
        <div class="card stat-card" style="border-top: 4px solid var(--color-secondary);">
            <div class="stat-value text-gradient-secondary">{{ total_reports }}</div>
            <div class="stat-label">Architecture Reports</div>
        </div>
        
        <div class="card stat-card" style="border-top: 4px solid var(--color-success);">
            <div class="stat-value" style="color: var(--color-success)">{{ latest_score|default:"-" }}</div>
            <div class="stat-label">Latest Architecture Score</div>
        </div>
    </div>
    
    <h3 class="animate-slide-up delay-200" style="margin-bottom: 1.5rem;">Recent Projects</h3>
    
    <div class="animate-slide-up delay-300">
        {% if projects %}
            <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 1.5rem;">
                {% for project in projects|slice:":6" %}
                <div class="card">
                    <h4 style="margin-bottom: 0.5rem;"><a href="{% url 'projects:project_detail' project.id %}">{{ project.name }}</a></h4>
                    <p style="color: var(--text-muted); margin-bottom: 1rem; font-size: 0.9rem;">
                        {{ project.description|truncatechars:80|default:"No description" }}
                    </p>
                    <div style="display: flex; justify-content: space-between; align-items: center; font-size: 0.85rem; color: var(--text-muted);">
                        <span>Updated: {{ project.updated_at|date:"M d, Y" }}</span>
                        {% if project.architecture_reports.first %}
                            <a href="{% url 'architecture:report_detail' project.architecture_reports.first.id %}" class="badge badge-tech">View Report</a>
                        {% else %}
                            <span class="badge" style="background: rgba(255,255,255,0.1)">Draft</span>
                        {% endif %}
                    </div>
                </div>
                {% endfor %}
            </div>
        {% else %}
            <div class="card text-center" style="padding: 4rem 2rem;">
                <p style="color: var(--text-muted); margin-bottom: 1.5rem;">You haven't created any architectures yet.</p>
                <a href="{% url 'projects:project_create' %}" class="btn btn-primary">Start First Project</a>
            </div>
        {% endif %}
    </div>
</div>
{% endblock %}
""",
    "templates/projects/project_form.html": """
{% extends 'base.html' %}

{% block extra_css %}
<style>
    .progress-container {
        display: flex;
        justify-content: space-between;
        margin-bottom: 3rem;
        position: relative;
    }
    
    .progress-container::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 0; right: 0;
        height: 2px;
        background: var(--color-border);
        z-index: 1;
        transform: translateY(-50%);
    }
    
    .progress-step {
        width: 30px; height: 30px;
        border-radius: 50%;
        background: var(--bg-card);
        border: 2px solid var(--color-border);
        display: flex; justify-content: center; align-items: center;
        z-index: 2;
        font-weight: 600; font-size: 0.85rem;
        transition: all 0.3s ease;
    }
    
    .progress-step.active {
        border-color: var(--color-primary);
        box-shadow: 0 0 10px var(--color-primary-glow);
        background: var(--color-primary);
        color: white;
    }
    
    .progress-step.completed {
        border-color: var(--color-primary);
        background: var(--bg-card);
        color: var(--color-primary);
    }
    
    .form-step {
        display: none;
    }
    
    .form-step.active {
        display: block;
    }
    
    #generation-overlay {
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(15, 23, 42, 0.9);
        backdrop-filter: blur(10px);
        z-index: 1000;
        display: none;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .loader {
        width: 60px; height: 60px;
        border: 4px solid rgba(6, 182, 212, 0.2);
        border-top-color: var(--color-primary);
        border-radius: 50%;
        animation: spin 1s linear infinite;
        margin-bottom: 2rem;
    }
    
    @keyframes spin { 100% { transform: rotate(360deg); } }
</style>
{% endblock %}

{% block content %}
<div id="generation-overlay">
    <div class="loader"></div>
    <h2 id="loading-message" class="text-gradient">Initializing AI Engine...</h2>
</div>

<div class="container" style="max-width: 800px; padding-top: 3rem; padding-bottom: 5rem;">
    <div class="card animate-slide-up">
        <h2 style="margin-bottom: 2rem;">Create Architecture</h2>
        
        <div class="progress-container">
            <div class="progress-step active">1</div>
            <div class="progress-step">2</div>
            <div class="progress-step">3</div>
            <div class="progress-step">4</div>
        </div>
        
        <form id="architecture-form">
            <!-- Step 1 -->
            <div class="form-step active" id="step-1">
                <h3>Project Information</h3>
                <div class="form-group">
                    <label class="form-label">Project Name</label>
                    <input type="text" id="p_name" class="form-control" required placeholder="e.g. HealthTracker Pro">
                </div>
                <div class="form-group">
                    <label class="form-label">Description</label>
                    <textarea id="p_desc" class="form-control" rows="3" required placeholder="Briefly describe what the application does..."></textarea>
                </div>
                <div class="form-group">
                    <label class="form-label">Application Type</label>
                    <select id="id_app_type" class="form-control">
                        <option value="web">Web Application</option>
                        <option value="mobile">Mobile Application</option>
                        <option value="ecommerce">E-Commerce</option>
                        <option value="ai">AI / Machine Learning</option>
                        <option value="saas">SaaS Platform</option>
                    </select>
                </div>
                
                <div id="conditional-ai" style="display: none; padding: 1rem; background: rgba(6, 182, 212, 0.05); border-left: 3px solid var(--color-primary); border-radius: 4px; margin-bottom: 1.5rem;">
                    <div class="form-group mb-0">
                        <label class="form-label">AI Integration Type</label>
                        <input type="text" id="p_ai_type" class="form-control" placeholder="e.g. LLM Chatbot, Image Generation, Recommendation Engine">
                    </div>
                </div>
                
                <div style="display: flex; justify-content: flex-end; margin-top: 2rem;">
                    <button type="button" class="btn btn-primary next-step">Next Step &rarr;</button>
                </div>
            </div>
            
            <!-- Step 2 -->
            <div class="form-step" id="step-2">
                <h3>Technical Preferences</h3>
                <div class="form-group">
                    <label class="form-label">Key Features</label>
                    <textarea id="p_features" class="form-control" rows="3" placeholder="Real-time chat, payment processing, video streaming..."></textarea>
                </div>
                <div class="form-group">
                    <label class="form-label">Technology Preferences (Optional)</label>
                    <textarea id="p_tech" class="form-control" rows="2" placeholder="e.g. prefer Python/Django, prefer PostgreSQL..."></textarea>
                </div>
                <div style="display: flex; justify-content: space-between; margin-top: 2rem;">
                    <button type="button" class="btn btn-secondary prev-step">&larr; Previous</button>
                    <button type="button" class="btn btn-primary next-step">Next Step &rarr;</button>
                </div>
            </div>
            
            <!-- Step 3 -->
            <div class="form-step" id="step-3">
                <h3>Scale & Infrastructure</h3>
                <div class="form-group">
                    <label class="form-label">Expected Users (Month 1)</label>
                    <select id="p_users" class="form-control">
                        <option value="1-1k">1 - 1,000</option>
                        <option value="1k-10k">1,000 - 10,000</option>
                        <option value="10k-100k">10,000 - 100,000</option>
                        <option value="100k+">100,000+</option>
                    </select>
                </div>
                <div class="form-group">
                    <label class="form-label">Infrastructure Requirements</label>
                    <textarea id="p_infra" class="form-control" rows="2" placeholder="e.g. AWS preferred, Docker required..."></textarea>
                </div>
                <div class="form-group">
                    <label class="form-label">Scalability Requirements</label>
                    <textarea id="p_scale" class="form-control" rows="2" placeholder="e.g. High availability, multi-region..."></textarea>
                </div>
                <div style="display: flex; justify-content: space-between; margin-top: 2rem;">
                    <button type="button" class="btn btn-secondary prev-step">&larr; Previous</button>
                    <button type="button" class="btn btn-primary next-step">Next Step &rarr;</button>
                </div>
            </div>
            
            <!-- Step 4 -->
            <div class="form-step" id="step-4">
                <h3>Security & Review</h3>
                <div class="form-group">
                    <label class="form-label">Security & Compliance</label>
                    <textarea id="p_sec" class="form-control" rows="3" placeholder="e.g. HIPAA compliance, end-to-end encryption..."></textarea>
                </div>
                
                <div class="card" style="background: rgba(6, 182, 212, 0.05); border-color: var(--color-primary); margin-bottom: 2rem;">
                    <h4 style="color: var(--color-primary); margin-bottom: 0.5rem;">Ready to Generate</h4>
                    <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 0;">Our AI Engine will now analyze your requirements and construct a complete production-grade architecture recommendation.</p>
                </div>
                
                <div style="display: flex; justify-content: space-between; margin-top: 2rem;">
                    <button type="button" class="btn btn-secondary prev-step">&larr; Previous</button>
                    <button type="submit" class="btn btn-primary" id="generate-btn">
                        <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                        Generate Architecture
                    </button>
                </div>
            </div>
        </form>
    </div>
</div>

{% endblock %}
{% block extra_js %}
<script src="/static/js/form.js"></script>
<script>
document.getElementById('architecture-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const data = {
        name: document.getElementById('p_name').value,
        description: document.getElementById('p_desc').value,
        app_type: document.getElementById('id_app_type').value,
        features: document.getElementById('p_features').value,
        tech_preferences: document.getElementById('p_tech').value,
        expected_users: document.getElementById('p_users').value,
        infrastructure_requirements: document.getElementById('p_infra').value,
        scalability_requirements: document.getElementById('p_scale').value,
        security_requirements: document.getElementById('p_sec').value,
    };
    
    try {
        const createRes = await fetch('/api/project/create/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}'
            },
            body: JSON.stringify(data)
        });
        const createData = await createRes.json();
        
        const genRes = await fetch(`/api/architecture/generate/${createData.project_id}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': '{{ csrf_token }}'
            }
        });
        const genData = await genRes.json();
        const reportId = genData.report_id;
        
        // Poll for completion
        const interval = setInterval(async () => {
            const statusRes = await fetch(`/api/architecture/status/${reportId}/`);
            const statusData = await statusRes.json();
            
            if (statusData.status === 'completed') {
                clearInterval(interval);
                window.location.href = `/architecture/report/${reportId}/`;
            } else if (statusData.status === 'failed') {
                clearInterval(interval);
                alert("Generation failed. Check server logs.");
                document.getElementById('generation-overlay').style.display = 'none';
            }
        }, 3000);
        
    } catch(err) {
        console.error(err);
        alert("An error occurred.");
        document.getElementById('generation-overlay').style.display = 'none';
    }
});
</script>
{% endblock %}
""",
    "templates/projects/project_detail.html": """
{% extends 'base.html' %}
{% block content %}
<div class="container" style="padding: 3rem 0;">
    <div class="card animate-slide-up">
        <h2>{{ object.name }}</h2>
        <p>{{ object.description }}</p>
        <p class="text-muted">Type: {{ object.requirement.app_type }}</p>
        
        <h3 style="margin-top:2rem;">Architecture Reports</h3>
        {% if object.architecture_reports.exists %}
            <ul>
                {% for r in object.architecture_reports.all %}
                    <li>
                        <a href="{% url 'architecture:report_detail' r.id %}">Report {{ r.created_at|date:"Y-m-d H:i" }}</a> 
                        - Score: {{ r.architecture_score }}
                    </li>
                {% endfor %}
            </ul>
        {% else %}
            <p>No reports generated yet.</p>
        {% endif %}
    </div>
</div>
{% endblock %}
""",
    "templates/architecture/report.html": """
{% extends 'base.html' %}

{% block extra_css %}
<style>
    .report-header {
        background: linear-gradient(to bottom, rgba(15, 23, 42, 1), var(--bg-card));
        padding: 4rem 0;
        border-bottom: 1px solid var(--color-border);
        margin-bottom: 3rem;
    }
    
    .score-circle {
        width: 120px; height: 120px;
        border-radius: 50%;
        background: var(--bg-dark);
        border: 4px solid var(--color-success);
        display: flex; justify-content: center; align-items: center;
        flex-direction: column;
        box-shadow: 0 0 30px rgba(16, 185, 129, 0.2);
    }
    
    .score-value {
        font-size: 2.5rem; font-weight: 800; color: var(--color-success); line-height: 1;
    }
    .score-label {
        font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 1px; margin-top: 0.25rem;
    }
    
    .section-title {
        display: flex; align-items: center; gap: 1rem;
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid var(--color-border);
    }
    
    .tech-item {
        background: rgba(255,255,255,0.03);
        border: 1px solid var(--color-border);
        border-radius: 8px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
</style>
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
{% endblock %}

{% block content %}
<div class="report-header animate-slide-up">
    <div class="container">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 2rem;">
            <div>
                <div class="badge badge-tech" style="margin-bottom: 1rem;">Architecture Report</div>
                <h1 style="font-size: 2.5rem; margin-bottom: 0.5rem;">{{ report.project.name }}</h1>
                <p style="color: var(--text-muted); max-width: 600px;">Generated on {{ report.created_at|date:"F j, Y, g:i a" }}</p>
            </div>
            
            <div class="score-circle">
                <div class="score-value">{{ report.architecture_score }}</div>
                <div class="score-label">Score</div>
            </div>
        </div>
        
        <div class="card" style="margin-top: 2rem; background: rgba(6, 182, 212, 0.05); border-color: rgba(6, 182, 212, 0.2);">
            <p style="margin: 0; font-size: 1.1rem; line-height: 1.7;">{{ report.summary }}</p>
        </div>
    </div>
</div>

<div class="container pb-5" style="padding-bottom: 5rem;">

    <!-- Diagram -->
    <section class="mb-5 animate-slide-up reveal" style="margin-bottom: 4rem;">
        <h2 class="section-title" style="color: var(--color-primary);">Architecture Diagram</h2>
        <div class="card" style="overflow-x: auto; text-align: center; background: #0f172a;">
            <div class="mermaid">
                {{ report.diagram_data|safe }}
            </div>
        </div>
    </section>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 2rem; margin-bottom: 4rem;">
        <!-- Technology Stack -->
        <section class="animate-slide-up reveal">
            <h2 class="section-title" style="color: var(--color-primary);">Technology Stack</h2>
            {% for tech in report.technology_stack %}
                <div class="tech-item">
                    <h4 style="color: var(--color-primary); margin-bottom: 0.5rem;">{{ tech.name }}</h4>
                    <p style="font-size: 0.9rem; margin-bottom: 0.5rem;"><strong>Use:</strong> {{ tech.description }}</p>
                    <p style="font-size: 0.85rem; color: var(--text-muted); margin: 0;"><em>Rationale: {{ tech.rationale }}</em></p>
                </div>
            {% endfor %}
        </section>

        <!-- Database -->
        <section class="animate-slide-up reveal">
            <h2 class="section-title" style="color: var(--color-secondary);">Database Design</h2>
            <div class="card" style="border-left: 4px solid var(--color-secondary);">
                <p><strong>Primary Database:</strong> {{ report.database_design.primary_database }}</p>
                {% if report.database_design.caching_layer %}
                <p><strong>Caching Layer:</strong> {{ report.database_design.caching_layer }}</p>
                {% endif %}
                <p style="font-size: 0.95rem; margin: 1rem 0;">{{ report.database_design.description }}</p>
                <div style="margin-top: 1rem;">
                    <strong>Key Collections/Tables:</strong>
                    <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.5rem;">
                    {% for t in report.database_design.key_tables_collections %}
                        <span class="badge badge-db">{{ t }}</span>
                    {% endfor %}
                    </div>
                </div>
            </div>
        </section>
        
        <!-- API -->
        <section class="animate-slide-up reveal">
            <h2 class="section-title" style="color: var(--color-api);">API Architecture</h2>
            <div class="card" style="border-left: 4px solid var(--color-api);">
                <p><strong>Style:</strong> {{ report.api_architecture.style }}</p>
                <p><strong>Auth:</strong> {{ report.api_architecture.authentication }}</p>
                <p style="font-size: 0.95rem; margin: 1rem 0;">{{ report.api_architecture.description }}</p>
                <ul style="padding-left: 1.5rem; color: var(--text-muted); font-size: 0.9rem;">
                {% for ep in report.api_architecture.endpoints_summary %}
                    <li>{{ ep }}</li>
                {% endfor %}
                </ul>
            </div>
        </section>
        
        <!-- Cloud -->
        <section class="animate-slide-up reveal">
            <h2 class="section-title" style="color: var(--color-cloud);">Cloud Architecture</h2>
            <div class="card" style="border-left: 4px solid var(--color-cloud);">
                <p><strong>Provider:</strong> {{ report.cloud_architecture.provider }}</p>
                <p><strong>Compute:</strong> {{ report.cloud_architecture.compute }}</p>
                <p><strong>Storage:</strong> {{ report.cloud_architecture.storage }}</p>
                <p style="font-size: 0.95rem; margin: 1rem 0; color: var(--text-muted);">{{ report.cloud_architecture.description }}</p>
            </div>
        </section>
    </div>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-bottom: 4rem;">
        <div class="card animate-slide-up reveal" style="border-color: rgba(16, 185, 129, 0.3);">
            <h3 style="color: var(--color-success);">Strengths</h3>
            <ul style="padding-left: 1.2rem; margin-top: 1rem; color: var(--text-muted);">
                {% for s in report.strengths %}<li>{{ s }}</li>{% endfor %}
            </ul>
        </div>
        <div class="card animate-slide-up reveal" style="border-color: rgba(239, 68, 68, 0.3);">
            <h3 style="color: var(--color-security);">Risks & Gotchas</h3>
            <ul style="padding-left: 1.2rem; margin-top: 1rem; color: var(--text-muted);">
                {% for r in report.risks %}<li>{{ r }}</li>{% endfor %}
            </ul>
        </div>
        <div class="card animate-slide-up reveal" style="border-color: rgba(245, 158, 11, 0.3);">
            <h3 style="color: var(--color-cloud);">Recommended Improvements</h3>
            <ul style="padding-left: 1.2rem; margin-top: 1rem; color: var(--text-muted);">
                {% for i in report.improvements %}<li>{{ i }}</li>{% endfor %}
            </ul>
        </div>
    </div>
    
    <!-- Security & Scale -->
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 2rem;">
        <section class="animate-slide-up reveal">
            <h2 class="section-title" style="color: var(--color-security);">Security Checklist</h2>
            <div class="card">
                {% for sec in report.security_checklist %}
                    <div style="margin-bottom: 1.5rem;">
                        <h4 style="color: var(--text-main); margin-bottom: 0.5rem;">{{ sec.category }}</h4>
                        <ul style="padding-left: 1.2rem; color: var(--text-muted); font-size: 0.9rem;">
                            {% for rec in sec.recommendations %}<li>{{ rec }}</li>{% endfor %}
                        </ul>
                    </div>
                {% endfor %}
            </div>
        </section>
        
        <section class="animate-slide-up reveal">
            <h2 class="section-title" style="color: var(--color-success);">Scalability Strategy</h2>
            <div class="card">
                <ul style="padding-left: 1.2rem; color: var(--text-muted); line-height: 1.8;">
                    {% for scale in report.scalability_strategy %}<li>{{ scale }}</li>{% endfor %}
                </ul>
            </div>
        </section>
    </div>
</div>
{% endblock %}

{% block extra_js %}
<script src="/static/js/diagrams.js"></script>
{% endblock %}
""",
    "templates/architecture/report_history.html": """
{% extends 'base.html' %}
{% block content %}
<div class="container">
    <h2>History for {{ project.name }}</h2>
    <ul>
        {% for report in reports %}
            <li><a href="{% url 'architecture:report_detail' report.id %}">{{ report.created_at }}</a> - Score: {{ report.architecture_score }}</li>
        {% endfor %}
    </ul>
</div>
{% endblock %}
"""
}

for filepath, content in FILES.items():
    create_file(filepath, content)
    print(f"Created {filepath}")

print("Frontend scaffold done.")
