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
    commit('addEmployee', response.data)
    console.log(response.data)
  })
}

// const addEmployee = ({ commit }, payload) => {
//   // axios.post('http://localhost:8000/api/crm/user/', payload)
//   axios.post(endpoint, payload)
//   .then(response => {
//     commit('addEmployee', response.data)
//     console.log(response.data)
//   })
// }

// const addEmployee = ({ commit }, payload) => {
//   axios.post('http://localhost:8000/api/crm/user/', payload)
//   .then(response => {
//     console.log('response', response);
//     axios.post(endpoint, {slug: payload.slug, user_ptr_id:response.data.pk})
//     console.log('payload', payload)
//     .then(response => {
//       commit('addEmployee', response.data)
//     })
//   })
// }

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