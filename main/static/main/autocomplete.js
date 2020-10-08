const form = document.querySelector('.searchbar');
const input = document.querySelector('input');
const autocompleteContainer = document.querySelector('.autocomplete-container');
const loadingModal = document.querySelector('.loading-modal');
const searchClear = document.getElementById('search-clear');
const submitBtn = document.querySelector('form button');

let newSuggestions = false;


if (input.value) searchClear.style.visibility = 'visible';

input.addEventListener('input', () => {
	if (input.value) searchClear.style.visibility = 'visible';
	else searchClear.style.visibility = 'hidden';
	if (input.value.length >= 3) autocomplete(input.value);
});

input.addEventListener('keyup', () => {
	if (!input.value) updateSuggestions([]);
});

input.addEventListener('click', () => {
	document.querySelectorAll('.suggestion').forEach(suggestion => {
		suggestion.style.visibility = 'visible';
	});
});

submitBtn.addEventListener('click', event => {
	event.preventDefault();
	if (input.value.length >= 3) {
		form.submit();
		setTimeout(() => {
			loadingModal.style.visibility = 'visible';
		}, 500);
	}
});

searchClear.addEventListener('click', () => {
	input.value = '';
	searchClear.style.visibility = 'hidden';
	updateSuggestions([]);
	input.focus();
});

window.addEventListener('keydown', event => keyEvent(event));

window.addEventListener('click', event => {
	if (event.target !== input) {
		document.querySelectorAll('.suggestion').forEach(suggestion => {
			suggestion.style.visibility = 'hidden';
		});
	}
});

window.addEventListener('mousemove', () => {
	if (newSuggestions) {
		document.querySelectorAll('.suggestion').forEach(suggestion => {
			suggestion.addEventListener('mouseover', () => focus(suggestion));
		});
		newSuggestions = false;
	}
});

function autocomplete(text) {
	const categories = "City,Metro%20Area,Subregion,Region,Territory,Country,Zone";
	const url = `http://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/suggest?text=${text}&category=${categories}&f=json`;
	const params = {mode: 'no-cors'}

	fetch(url, params).then(response => {
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
		autocompleteContainer.appendChild(newDiv);
	});

	if (suggestions.length > 0) {
		document.querySelector('.suggestion').classList.add('focused');
		newSuggestions = true;
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