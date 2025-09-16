document.addEventListener('DOMContentLoaded', function() {
    const uploadArea = document.getElementById('uploadArea');
    const fileInput = document.getElementById('fileInput');
    const emailText = document.getElementById('emailText');
    const processBtn = document.getElementById('processBtn');
    const clearBtn = document.getElementById('clearBtn');
    const uploadText = document.getElementById('uploadText');
    const fileBadge = document.getElementById('fileBadge');
    const fileName = document.getElementById('fileName');
    const processText = document.getElementById('processText');
    const form = document.getElementById('emailForm');

    // File upload functionality
    function handleFile(file) {
        if (file && (file.type === 'text/plain' || file.type === 'application/pdf')) {
            fileName.textContent = file.name;
            fileBadge.style.display = 'block';
            uploadText.textContent = file.name;
            updateButtons();
        }
    }

    // Drag and drop
    uploadArea.addEventListener('dragover', function(e) {
        e.preventDefault();
        uploadArea.classList.add('drag-over');
    });

    uploadArea.addEventListener('dragleave', function(e) {
        e.preventDefault();
        uploadArea.classList.remove('drag-over');
    });

    uploadArea.addEventListener('drop', function(e) {
        e.preventDefault();
        uploadArea.classList.remove('drag-over');
        
        const files = Array.from(e.dataTransfer.files);
        const validFile = files.find(f => 
            f.type === 'text/plain' || f.type === 'application/pdf'
        );
        
        if (validFile) {
            fileInput.files = e.dataTransfer.files;
            handleFile(validFile);
        }
    });

    // File input change
    fileInput.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (file) {
            handleFile(file);
        }
    });

    // Text area input
    emailText.addEventListener('input', function() {
        updateButtons();
    });

    // Update button states
    function updateButtons() {
        const hasFile = fileInput.files && fileInput.files.length > 0;
        const hasText = emailText.value.trim().length > 0;
        const hasContent = hasFile || hasText;
        
        processBtn.disabled = !hasContent;
        clearBtn.style.display = hasContent ? 'block' : 'none';
    }

    // Clear form
    clearBtn.addEventListener('click', function() {
        fileInput.value = '';
        emailText.value = '';
        fileBadge.style.display = 'none';
        uploadText.textContent = 'Arraste um arquivo aqui ou clique para selecionar';
        updateButtons();
    });

    // Form submission with loading state
    form.addEventListener('submit', function(e) {
        processBtn.disabled = true;
        processBtn.classList.add('processing');
        processText.innerHTML = `
            <div style="width: 1rem; height: 1rem; border: 2px solid rgba(255,255,255,0.2); border-top: 2px solid white; border-radius: 50%; animation: spin 1s linear infinite; margin-right: 0.5rem;"></div>
            Processando...
        `;
    });

    // Initial button state
    updateButtons();
});