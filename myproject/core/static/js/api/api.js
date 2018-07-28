axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

export default {
    subtotal
};

function subtotal(u, r){
    return 42
};

function get(url, params){
    return axios.get(url, {params: params})
}

function post(url, params){
    var fd = new FormData();
    Object.keys(params).map((k) => {
        fd.append(k, params[k]);
    })
    return axios.post(url, fd);
}
