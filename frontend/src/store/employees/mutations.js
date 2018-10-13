const setEmployees = (state, payload) => {
  state.employees = payload
}

const deleteEmployee = (state, payload) => {
  // axios.delete('http://localhost:8000/api/crm/employee/' + this.deletingItem.pk)
  // .then(response => {
    const idx = state.employees.indexOf(payload)
    state.employees.splice(idx, 1)
  // })
}

export default {
  setEmployees,
  deleteEmployee,
}