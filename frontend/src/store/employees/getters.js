const getEmployeeById = (state) => {
  return (id) => {
    return state.employees.find(e => {
      return e.pk == id
    })
  }
}

export default {
  getEmployeeById,
}