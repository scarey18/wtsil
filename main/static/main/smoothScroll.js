const homeLogo = document.querySelector('#home-logo');
const hero = document.querySelector('.hero');
const arrowDown = document.querySelector('#arrow-down');
const arrowUp = document.querySelector('#arrow-up');
const fixedArrow = document.querySelector('.fixed-arrow');

window.addEventListener('scroll', () => {
	if (window.scrollY > window.innerHeight) fixedArrow.style.visibility = 'visible';
	else fixedArrow.style.visibility = 'hidden';
});

[homeLogo, arrowDown].forEach(element => {
	if (!element) return;
	element.addEventListener('click', () => {
		window.scrollTo({
			top: window.scrollY + hero.getBoundingClientRect().top,
			behavior: 'smooth',
		});
	});
});

arrowUp.addEventListener('click', () => {
	window.scrollTo({
		top: 0,
		behavior: 'smooth',
	});
});