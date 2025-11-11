// Simple markdown renderer for legal pages
function renderMarkdown(markdown) {
    let html = markdown;
    
    // Headers
    html = html.replace(/^# (.*$)/gim, '<h1 style="color: #ffffff; font-size: 2.5rem; margin-bottom: 1rem; font-weight: 700;">$1</h1>');
    html = html.replace(/^## (.*$)/gim, '<h2 style="color: #00f5ff; font-size: 1.5rem; margin-bottom: 1rem; font-weight: 600; margin-top: 2.5rem;">$2</h2>');
    html = html.replace(/^### (.*$)/gim, '<h3 style="color: #00f5ff; font-size: 1.25rem; margin-bottom: 0.75rem; font-weight: 600; margin-top: 1.5rem;">$3</h3>');
    
    // Bold text
    html = html.replace(/\*\*(.*?)\*\*/gim, '<strong style="color: #ffffff;">$1</strong>');
    
    // Links
    html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/gim, '<a href="$2" style="color: #00f5ff; text-decoration: none;">$1</a>');
    
    // Unordered lists
    html = html.replace(/^\- (.+)$/gim, '<li style="position: relative; margin-bottom: 0.5rem; padding-left: 1.5rem;"><span style="position: absolute; left: 0; color: #00f5ff;">•</span>$1</li>');
    html = html.replace(/(<li[^>]*>.*<\/li>)/s, '<ul style="list-style: none; padding-left: 1.5rem; margin-bottom: 1rem;">$1</ul>');
    
    // Paragraphs
    html = html.replace(/^(?!<[hul]|<strong)(.*$)/gim, '<p style="margin-bottom: 1rem; line-height: 1.8; color: #c0c0c0;">$1</p>');
    
    // Clean up empty paragraphs
    html = html.replace(/<p[^>]*>\s*<\/p>/gim, '');
    
    return html;
}

// Load markdown content
async function loadMarkdownContent(markdownPath, containerId) {
    try {
        const response = await fetch(markdownPath);
        const markdown = await response.text();
        const html = renderMarkdown(markdown);
        document.getElementById(containerId).innerHTML = html;
    } catch (error) {
        console.error('Error loading markdown:', error);
        document.getElementById(containerId).innerHTML = '<p style="color: #ff6b6b;">Error loading content. Please try again later.</p>';
    }
}
