<template>
  <div>
    Employees
    
    <!-- <b-table striped hover :items="items"></b-table> -->
    <table class="table">
      <thead>
        <tr>
          <th>#</th>
          <th>Slug</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items">
          <td>{{ item.pk }}</td>
          <td>{{ item.slug }}</td>
          <td>
            <b-btn variant="link" v-b-modal.modal1 @click="deletingItem=item">
              <i class="fa fa-close" style="color:red"></i>
            </b-btn>
          </td>
        </tr>
      </tbody>
    </table>

    <b-modal id="modal1" title="Bootstrap-Vue" @ok="deleteItem">
      <p class="my-4">Deseja mesmo apagar {{ deletingItem.slug }}?</p>
    </b-modal>

  </div>
</template>

<script>

import axios from 'axios'

export default {
  data () {
    return {
      items: [],
      deletingItem: {}
    }
  },
  async created(){
    this.$store.dispatch('getEmployees')
  },
  methods: {
    deleteItem() {
      // axios.delete('http://localhost:8000/api/crm/employee/' + this.deletingItem.pk)
      // .then(response => {
        const idx = this.items.indexOf(this.deletingItem)
        this.items.splice(idx, 1)
      // })
    }
  }
}
</script>