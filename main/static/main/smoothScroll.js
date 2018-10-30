const arrowDown = document.querySelector('#arrow-down');
const arrowUp = document.querySelector('#arrow-up');
const hero = document.querySelector('.hero');


arrowDown.addEventListener('click', () => {
	window.scrollTo({
		top: window.scrollY + hero.getBoundingClientRect().top,
		behavior: 'smooth',
	});
});

arrowUp.addEventListener('click', () => {
	window.scrollTo({
		top: 0,
		behavior: 'smooth',
	});
});