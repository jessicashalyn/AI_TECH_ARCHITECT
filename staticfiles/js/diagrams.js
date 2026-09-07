
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
