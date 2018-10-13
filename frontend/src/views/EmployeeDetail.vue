<template>
  <div>
    Employees
    
    {{ employee.pk }}
    {{ employee.slug }}

  </div>
</template>

<script>

export default {
  computed: {
    employee() {
      const id = this.$route.params.id
      return this.$store.getters.getEmployeeById(id)
    }
  }
}
</script>