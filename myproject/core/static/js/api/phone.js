Vue.config.delimiters = ['${', '}']

Vue.component('v-phone', {
  delimiters: ['${', '}'],
  mixins: [Mixin],
  // props: ['message'],
  props: {
      message: {
          type: String,
          default: ''
      },
      show: {
          type: Boolean,
          twoWay: true,
          default: false
      },
      title: {
          type: String,
          default: 'Modal'
      },
      // Bootstrap small style modal
      small: {
          type: Boolean,
          default: false
      },
      // Bootstrap large style modal
      large: {
          type: Boolean,
          default: false
      },
      // Bootstrap full style modal    
      full: {
          type: Boolean,
          default: false
      },
      // if it set false, click background will close modal 
      force: {
          type: Boolean,
          default: false
      },
      // vue transition name
      transition: {
          type: String,
          default: 'modal'
      },
      // [OK button] text
      okText: {
          type: String,
          default: 'OK'
      },
      // [Cancel button] text
      cancelText: {
          type: String,
          default: 'Cancel'
      },
      // [OK button] className
      okClass: {
          type: String,
          default: 'btn blue'
      },
      // [Cancel button] className
      cancelClass: {
          type: String,
          default: 'btn red btn-outline'
      },
      // automatically close when click [OK button]
      closeWhenOK: {
          type: Boolean,
          default: false
      }
  },
  data: () => ({
    show: false,
    employee: '',
    phones: [],
    url: '/crm/employee/phone/',
    url_add: '/crm/employee/phone/add/'
  }),
  methods: {
    get_phones(page){
      axios.get(this.url + page)
      .then((result) => {
        this.phones = result.data.map((item) => {
          return {pk: item.pk, phone: item.fields.phone, phone_type: item.fields.phone_type}
        })
      })
    }
  },
  save_phone(){
    let bodyFormData = new FormData()
    bodyFormData.append('employee', this.employee)
    bodyFormData.append('phone2', this.phone2)
    bodyFormData.append('phone_type', this.phone_type)
    // let config = {headers: {'Content-Type': 'multipart/form-data'}}
    if (!this.phone2) {
      this.message = 'Favor preencher o telefone.'
      setTimeout(()=>{
        this.message = ''
      }, 2000);
    } else {
      axios.post(url_add, bodyFormData)
      .then((response) => {
        this.phones.push(
          {
            phone: this.phone2,
            phone_type: this.phone_types_display[this.phone_type]
          }
        )
        this.phone2 = ''
        this.phone_type = ''
      })
    }
  },
  mounted(){
    // Mixin.teste()
    // this.employee = document.getElementById("app").getAttribute('data-pk')
    this.employee = window.location.pathname.match("[0-9]")[0]
    this.get_phones(this.employee)
  },
  template: `
    <div class="card">
      <div class="card-header">
        Telefones
        <span class="span-is-link badge badge-success float-right" data-target="#modalPhoneAdd" role="button" data-toggle="modal"><i class="fa fa-plus"></i> Adicionar</span>
      </div>
      <div class="card-body">
        <transition name="fade">
          <p id="alert" ref="alert" class="alert alert-warning" v-if="message" role="alert"><span style="font-weight:bold">\${ message }</span></p>
        </transition>
        <table class="table table-responsive-sm table-outline">
          <tbody>
            <tr v-for="phone in phones">
              <td>
                <div>\${ phone.phone }</div>
                <div class="small">\${ phone.phone_type }</div>
              </td>
              <!-- {% if not request.user|has_group:"simpleuser" %} -->
                <td style="padding:0">
                  <span class="span-is-link span-color-link" data-target="#modalPhoneEdit" data-toggle="modal" @click="load_phone(phone)">
                    <i class="fa fa-pencil-square-o"></i>
                  </span>
                </td>
                <td>
                  <form action="." method="POST">
                    <!-- {% csrf_token %} -->
                    <span class="span-is-link" @click="remove_phone(phone)">
                      <i class="fa fa-close" style="color:red"></i>
                    </span>
                  </form>
                </td>
              <!-- {% endif %} -->
            </tr>
          </tbody>
        </table>
      </div>
    </div> <!-- card -->

    <!-- modal -->
    <!-- https://vuejsexamples.com/bootstrap-style-modal-for-vue/ -->
    <modal title="modalPhoneEdit" :show.sync="show" @ok="ok" @cancel="cancel">
      <div>Modal Body</div>
      <div slot="header">Modal Header</div>
      <div slot="title">Modal Title</div>
      <div slot="footer">Modal Footer</div>
    </modal>
  `
})