const form = document.querySelector('.searchbar');
const input = document.querySelector('input');
const autocompleteContainer = document.querySelector('.autocomplete-container');
const loadingModal = document.querySelector('.loading-modal');
const submitBtn = document.querySelector('form button')


input.addEventListener('input', () => {
	if (input.value.length >= 3) autocomplete(input.value);
});

submitBtn.addEventListener('click', (e) => {
	e.preventDefault();
	if (input.value.length >= 3) {
		form.submit();
		setTimeout(() => {
			loadingModal.style.visibility = 'visible';
		}, 500);
	}
});

window.addEventListener('keydown', event => keyEvent(event));

window.addEventListener('click', event => {
	if (event.target !== input && input.value.length < 3) updateSuggestions([]);
});


function autocomplete(text) {
	const categories = "City,Metro%20Area,Subregion,Region,Territory,Country,Zone";
	const url = `http://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/suggest?text=${text}&category=${categories}&f=json`;

	fetch(url).then(response => {
		if (response.ok) return response.json();
	}).then(data => updateSuggestions(data.suggestions));
}

function updateSuggestions(suggestions) {
	document.querySelectorAll('.suggestion').forEach(suggestion => {
		autocompleteContainer.removeChild(suggestion);
	});

	suggestions.forEach(suggestion => {
		const newDiv = document.createElement('div');
		newDiv.classList.add('suggestion');
		newDiv.textContent = suggestion.text;
		newDiv.addEventListener('click', () => selectSuggestion(suggestion.text));
		newDiv.addEventListener('mouseover', () => focus(newDiv));
		autocompleteContainer.appendChild(newDiv);
	});

	if (suggestions.length > 0) {
		document.querySelector('.suggestion').classList.add('focused');
	}
}

function focus(suggestion) {
	const focused = document.querySelector('.focused');
	if (focused) focused.classList.remove('focused');
	suggestion.classList.add('focused');
	input.value = suggestion.textContent;
}

function selectSuggestion(text) {
	input.value = text;
	form.submit();
	setTimeout(() => {
		loadingModal.style.visibility = 'visible';
	}, 500);
}

function keyEvent(event) {
	const focused = document.querySelector('.focused');
	if (!focused) return;

	const suggestions = document.querySelectorAll('.suggestion');
	const firstSuggestion = suggestions[0];
	const lastSuggestion = suggestions[suggestions.length-1];

	switch (event.keyCode) {
		case 40: {
			event.preventDefault();
			const node = focused === lastSuggestion ? null : focused.nextSibling;
			if (node) focus(node);
			break;
		} 
		case 38: {
			event.preventDefault();
			const node = focused === firstSuggestion ? null : focused.previousSibling;
			if (node) focus(node);
			break;
		}
		case 13: selectSuggestion(focused.textContent);
	}
}