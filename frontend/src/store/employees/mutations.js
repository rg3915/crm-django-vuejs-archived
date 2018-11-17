import axios from 'axios'

const addEmployee = (state, payload) => {
  state.employees.unshift(payload);
}

const setEmployees = (state, payload) => {
  state.employees = payload
}

const deleteEmployee = (state, payload) => {
  const idx = state.employees.indexOf(payload)
  state.employees.splice(idx, 1)
}

export default {
  addEmployee,
  setEmployees,
  deleteEmployee,
}