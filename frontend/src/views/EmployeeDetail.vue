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
      return this.$store.state.employees.find(e => {
        return e.pk == this.$route.params.id
      })
    }
  }
}
</script>