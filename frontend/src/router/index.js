import Vue from 'vue'
import Router from 'vue-router'

import Index from '../views/Index.vue'
import Employees from '../views/Employees.vue'
import EmployeeDetail from '../views/EmployeeDetail.vue'
import EmployeeForm from '../views/EmployeeForm.vue'

Vue.use (Router)

export default new Router ({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index
    },
    {
      path: '/crm/employees',
      name: 'employees',
      component: Employees
    },
    {
      path: '/crm/employees/add',
      name: 'employeeCreate',
      component: EmployeeForm
    },
    {
      path: '/crm/employees/:id',
      name: 'employeeDetail',
      component: EmployeeDetail
    },
  ]
})