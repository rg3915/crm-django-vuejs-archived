<template>
  <div>
    Employees

    <div v-if="employee">
      {{ employee.pk }}
      {{ employee.slug }}
    </div>

    <div v-else>
      Funcionário não encontrado
    </div>

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