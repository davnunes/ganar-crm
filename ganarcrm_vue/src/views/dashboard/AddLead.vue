<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Leads</h1>
      </div>
      <div class="column is-12">
        <form @submit.prevent="submitForm">
            <div class="field">
                <label>Company</label>
                <div class="control">
                    <input type="text" class="input" v-model="company">
                </div>
            </div>
            <div class="field">
                <label>Contact Person</label>
                <div class="control">
                    <input type="text" class="input" v-model="contact_person">
                </div>
            </div>
            <div class="field">
                <label>Email</label>
                <div class="control">
                    <input type="text" class="input" v-model="email">
                </div>
            </div>
            <div class="field">
                <label>Website</label>
                <div class="control">
                    <input type="text" class="input" v-model="website">
                </div>
            </div>
            <div class="field">
                <label>Confidence</label>
                <div class="control">
                    <input type="number" class="input" v-model="confidence">
                </div>
            </div>
            <div class="field">
                <label>Estimated Value</label>
                <div class="control">
                    <input type="number" class="input" v-model="estimated_value">
                </div>
            </div>
            <div class="field">
                <label>Status</label>
                <div class="control">
                    <select class="select" v-model="status">
                        <option value="new">New</option>
                        <option value="contacted">Contacted</option>
                        <option value="inprogress">In Progress</option>
                        <option value="lost">Lost</option>
                        <option value="won">Won</option>
                    </select>
                </div>
            </div>
            <div class="field">
                <label>Priority</label>
                <div class="control">
                    <select class="select" v-model="priority">
                        <option value="low">Low</option>
                        <option value="medium">Medium</option>
                        <option value="high">High</option>
                    </select>
                </div>
            </div>
            <div class="field">
                <div class="control">
                    <button class="button is-success">Submit</button>
                </div>
            </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AddLead",
  data() {
    return {
        company: '',
        contact_person: '',
        email: '',
        phone: '',
        website: '',
        confidence: '',
        estimated_value: '',
        status: 'new',
        priority: 'medium'
    }
  },
  methods: {
    submitForm() {
        console.log('ioi')
        // todo: 1:29:14
    } 
  }
};
</script>
