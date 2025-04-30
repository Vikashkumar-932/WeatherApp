fetch('/static/data/cities.json').then(r=>r.json()).then(cities=>{
    const dl=document.createElement('datalist');dl.id='cities';document.body.append(dl);
    cities.forEach(c=>{let o=document.createElement('option');o.value=c;dl.append(o)});
    document.getElementById('city-input').setAttribute('list','cities');
  });
  