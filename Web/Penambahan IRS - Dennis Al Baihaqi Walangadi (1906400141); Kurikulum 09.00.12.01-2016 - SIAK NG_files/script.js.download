function expand(n) {
	var o = $('ul'+n);
	if (o != undefined) {
		var d = o.style.display;
		o.style.display = (d == 'none' ? 'block' : 'none');
		var i = $('img'+n);
		var btm = (i.src.match(/bottom/) ? 'bottom' : '');
		i.src = mypub + (d == 'none' ? 'minus'+btm+'.gif' : 'plus'+btm+'.gif');
		i = $('fld'+n);
		i.src = mypub + (d == 'none' ? 'open.gif' : 'folder.gif');
	}
}

var state = Array();
function selectRow(el, nr) {
	if (state[el.name] && state[el.name] == el.value) { 
		el.checked = false;
		state[el.name] = '';
		$('r'+nr).className = $('r'+nr).className.replace(' sel', '');
	} else { 
		el.checked = true; 
		state[el.name] = el.value;
		checkCheckbox(nr, el.name);
	}
	return true;
}

var state = Array();
function selectAddRow(el, nr) {
	if (state[el.name] && state[el.name] == el.value) { 
		el.checked = false;
		state[el.name] = '';
	} else { 
		el.checked = true; 
		state[el.name] = el.value;
	}
	return true;
}

/* Mark checkbox nr as selected and unmark all other checkbox with same name */
function checkCheckbox(nr, name) {
	var els, i, n;
	/* Reset classname */
	els = document.getElementsByName(name);
	for (i = 0; i < els.length; i++) {
		n = els[i].id.substring(1);
		$('r'+n).className = $('r'+n).className.replace(' sel', '');
	}
	$('r'+nr).className += ' sel';
}

