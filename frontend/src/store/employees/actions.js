import axios from 'axios'

const getEmployees = async ({ commit }) => {
  const response = await axios.get('http://localhost:8000/api/crm/employee/')
  const employees = response.data.map(item => {
    return {
      'pk': item.pk,
      'slug': item.slug,
    }
  })
  commit('setEmployees', employees)
}

const deleteEmployee = ({ commit }, payload) => {
  commit('deleteEmployee', payload)
}

export default {
  getEmployees,
  deleteEmployee,
}