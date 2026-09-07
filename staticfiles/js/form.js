
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
