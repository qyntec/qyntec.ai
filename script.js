// Netlify Form submission handler
const signupForm = document.getElementById('signupForm');
const successMessage = document.getElementById('successMessage');

if (signupForm) {
    signupForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const formData = new FormData(signupForm);
        const emailInput = document.getElementById('emailInput');
        const submitButton = signupForm.querySelector('button[type="submit"]');
        
        // Disable button during submission
        submitButton.disabled = true;
        submitButton.innerHTML = 'Submitting...';
        
        try {
            const response = await fetch('/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: new URLSearchParams(formData).toString()
            });
            
            if (response.ok) {
                // Show success message
                emailInput.value = '';
                successMessage.classList.add('show');
                
                // Hide success message after 5 seconds
                setTimeout(() => {
                    successMessage.classList.remove('show');
                }, 5000);
            } else {
                throw new Error('Form submission failed');
            }
        } catch (error) {
            console.error('Error:', error);
            showError('Something went wrong. Please try again.');
        } finally {
            // Re-enable button
            submitButton.disabled = false;
            submitButton.innerHTML = `
                Get Early Access
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                    <path d="M4 10H16M16 10L11 5M16 10L11 15" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
            `;
        }
    });
}

function showError(message) {
    const emailInput = document.getElementById('emailInput');
    const inputWrapper = emailInput.closest('.input-wrapper');
    
    // Add error styling
    inputWrapper.style.borderColor = '#ff4444';
    
    // Create or update error message
    let errorDiv = document.querySelector('.error-message');
    if (!errorDiv) {
        errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        errorDiv.style.cssText = `
            color: #ff4444;
            font-size: 0.875rem;
            margin-top: 0.5rem;
            text-align: center;
        `;
        inputWrapper.parentNode.insertBefore(errorDiv, inputWrapper.nextSibling);
    }
    errorDiv.textContent = message;
    
    // Remove error after 3 seconds
    setTimeout(() => {
        inputWrapper.style.borderColor = '';
        if (errorDiv) errorDiv.remove();
    }, 3000);
}

// Modal functions for footer links
function showComingSoon(title) {
    const modal = document.getElementById('modal');
    const modalBody = document.getElementById('modalBody');
    
    modalBody.innerHTML = `
        <h2 style="font-size: 1.75rem; font-weight: 700; margin-bottom: 1rem; background: linear-gradient(135deg, #00f5ff, #0066ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">
            ${title}
        </h2>
        <p style="color: #a0a0a0; line-height: 1.6; margin-bottom: 1.5rem;">
            We're still putting the finishing touches on our ${title.toLowerCase()}. 
            Sign up for early access to be notified when we launch!
        </p>
        <button class="btn-primary" onclick="closeModal()" style="width: 100%; justify-content: center;">
            Got it
        </button>
    `;
    
    modal.classList.add('show');
    document.body.style.overflow = 'hidden';
}

function showContactInfo() {
    const modal = document.getElementById('modal');
    const modalBody = document.getElementById('modalBody');
    
    modalBody.innerHTML = `
        <h2 style="font-size: 1.75rem; font-weight: 700; margin-bottom: 1rem; background: linear-gradient(135deg, #00f5ff, #0066ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">
            Get in Touch
        </h2>
        <p style="color: #a0a0a0; line-height: 1.6; margin-bottom: 1.5rem;">
            Interested in learning more about our platform? Sign up for early access and we'll reach out with more details.
        </p>
        <p style="color: #ffffff; margin-bottom: 1.5rem;">
            For partnership inquiries, please email:<br>
            <a href="mailto:partnerships@healthtech.com" style="color: #00f5ff; text-decoration: none;">
                partnerships@healthtech.com
            </a>
        </p>
        <button class="btn-primary" onclick="closeModal()" style="width: 100%; justify-content: center;">
            Close
        </button>
    `;
    
    modal.classList.add('show');
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    const modal = document.getElementById('modal');
    modal.classList.remove('show');
    document.body.style.overflow = '';
}

// Close modal on outside click
document.getElementById('modal')?.addEventListener('click', function(e) {
    if (e.target === this) {
        closeModal();
    }
});

// Close modal on Escape key
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closeModal();
    }
});

// Smooth scroll for footer links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add parallax effect to gradient orbs on mouse move
document.addEventListener('mousemove', (e) => {
    const orbs = document.querySelectorAll('.gradient-orb');
    const mouseX = e.clientX / window.innerWidth;
    const mouseY = e.clientY / window.innerHeight;
    
    orbs.forEach((orb, index) => {
        const speed = (index + 1) * 0.05;
        const x = (mouseX - 0.5) * 50 * speed;
        const y = (mouseY - 0.5) * 50 * speed;
        
        orb.style.transform = `translate(${x}px, ${y}px)`;
    });
});

// Intersection Observer for fade-in animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe all feature cards
document.querySelectorAll('.feature-card').forEach(card => {
    observer.observe(card);
});

// Add loading state
window.addEventListener('load', () => {
    document.body.classList.add('loaded');
});
