document.getElementById('loc-btn').onclick = ()=>{
    navigator.geolocation.getCurrentPosition(p=>{
      window.location=`/?lat=${p.coords.latitude}&lon=${p.coords.longitude}`;
    });
  };
  