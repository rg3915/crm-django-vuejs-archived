<template>
  <div>
    Employees
    
    <form action="" @submit.prevent="addItem()" method="POST">
      <label>slug</label>
      <input id="id_slug" class="form-control" type="text" v-model="form.slug" />

      <label>username</label>
      <input id="id_username" class="form-control" type="text" v-model="form.username" />

      <label>first_name</label>
      <input id="id_first_name" class="form-control" type="text" v-model="form.first_name" />

      <label>last_name</label>
      <input id="id_last_name" class="form-control" type="text" v-model="form.last_name" />

      <label>email</label>
      <input id="id_email" class="form-control" type="text" v-model="form.email" />

      <label>password</label>
      <input id="id_password" class="form-control" type="text" v-model="form.password" />

      <label>personal_email</label>
      <input id="id_personal_email" class="form-control" type="text" v-model="form.personal_email" />

      <button type="submit" class="btn btn-primary">Salvar</button>
    </form>

  </div>
</template>

<script>

export default {
  data () {
    return {
      form: {}
    }
  },
  methods: {
    addItem() {
      this.$store.dispatch('addEmployee', this.form)
        this.$router.push('/crm/employees')
    }
  }
}
</script>