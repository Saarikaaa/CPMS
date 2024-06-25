document.addEventListener('DOMContentLoaded', function() {
    var industrySelect = document.getElementById('industry_type');
    var hiddenInput = document.getElementById('industry_type_hidden');

    industrySelect.addEventListener('change', function() {
        var selectedOption = industrySelect.options[industrySelect.selectedIndex];
        var industryString = selectedOption.dataset.industry;
        hiddenInput.value = industryString;
    });
});
