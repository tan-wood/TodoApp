

<script>
import { defineComponent } from 'vue';
import { mapActions } from 'vuex';

export default defineComponent({
    name: 'Login',
    data(){
        return{
            form:{
                username: '',
                password: '',
            }
        };
    }, 
    methods:{
        ...mapActions(['logIn']),
        async submit(){
            const User = new FormData();
            User.append('username', this.form.username);
            User.append('password', this.form.password);
            await this.logIn(User);
            this.$router.push('/dashboard');
        }
    }
});
</script>