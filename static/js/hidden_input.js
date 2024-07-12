document.getElementById('stop-words').addEventListener('change', function() {
    if (this.value === 'custom') {
        var tempFileInput = document.createElement('input');
        tempFileInput.type = 'file';
        tempFileInput.accept = '.txt';
        tempFileInput.style.display = 'none';

        tempFileInput.addEventListener('change', function(e) {
            var file = e.target.files[0];
            if (file) {
                var selectElement = document.getElementById('stop-words');
                var newOption = document.createElement('option');
                newOption.value = 'uploaded';
                newOption.text = '停词文件: ' + file.name;
                newOption.selected = true;

                selectElement.remove(selectElement.length - 1);
                selectElement.add(newOption);

                console.log('Selected file:', file.name);
            }
        });

        document.body.appendChild(tempFileInput);
        tempFileInput.click();
        document.body.removeChild(tempFileInput);
    }
});
