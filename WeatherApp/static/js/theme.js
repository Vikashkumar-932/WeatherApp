const t=document.getElementById('theme-toggle');
if(localStorage.theme==='dark')t.checked=true,document.documentElement.setAttribute('data-theme','dark');
t.onchange=()=>{const th=t.checked?'dark':'light';document.documentElement.setAttribute('data-theme',th);localStorage.theme=th;};
