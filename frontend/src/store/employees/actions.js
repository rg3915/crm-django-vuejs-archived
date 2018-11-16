import axios from 'axios'

const getEmployees = async ({ commit }) => {
  const url = 'http://localhost:8000/api/crm/employee/'
  const response = await axios.get(url)
  const employees = response.data.map(item => {
    return {
      'pk': item.pk,
      'slug': item.slug,
    }
  })
  commit('setEmployees', employees)
}

const deleteEmployee = ({ commit }, payload) => {
  const url = `http://localhost:8000/api/crm/employee/${payload.pk}/`
  axios.delete(url)
  .then(response => {
    commit('deleteEmployee', payload)
  })
}

export default {
  getEmployees,
  deleteEmployee,
}