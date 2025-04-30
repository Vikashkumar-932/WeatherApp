const hist=JSON.parse(localStorage.history||'[]'),c=document.querySelector('.container');
hist.slice(-5).forEach(city=>{let b=document.createElement('button');b.textContent=city;b.onclick=()=>document.getElementById('city-input').value=city;c.append(b)});
document.querySelector('form').onsubmit=()=>{hist.push(document.getElementById('city-input').value);localStorage.history=JSON.stringify(hist.slice(-10))};
