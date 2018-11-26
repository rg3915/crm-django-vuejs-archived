import axios from 'axios'

const endpoint = 'http://localhost:8000/api/crm/employee/'

const getEmployees = async ({ commit }) => {
  const response = await axios.get(endpoint)
  const employees = response.data.map(item => {
    return {
      'pk': item.pk,
      'slug': item.slug,
    }
  })
  commit('setEmployees', employees)
}

const addEmployee = ({ commit }, payload) => {
  axios.post('http://localhost:8000/api/crm/user/', payload)
  .then(response => {
    const pk = response.data.pk
    axios.post(endpoint, {slug: payload.slug, user: pk})
    .then(res => {
      commit('addEmployee', {slug: res.data.slug, pk: res.data.pk})
    })
  })
}

const deleteEmployee = ({ commit }, payload) => {
  const url = `${endpoint}${payload.pk}/`
  axios.delete(url)
  .then(() => {
    commit('deleteEmployee', payload)
  })
}

export default {
  getEmployees,
  addEmployee,
  deleteEmployee,
}