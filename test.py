import streamlit as st

#sidebar judul
st.sidebar.header("GAS MULIA")
st.sidebar.image('Gas Mulia.png',width=200)
test = st.sidebar.selectbox(
    "Navigation",
    ("Home🏠", "About Noble Gas👨‍🔬", "Noble Gas Identification🔬"))
st.sidebar.write("© Kelompok 10")

#Halaman home
if test == "Home🏠":
    #foto
    st.image('Identifikasi.png')
    st.title('Gas Mulia')
    st.write('Selamat Datang!')
    st.write('Aplikasi ini dibuat bertujuan untuk mengetahui info mengenai atom Gas Mulia dengan menginput nama Atom Gas Mulia yang ingin diketahui')
    #List Kelompok
    st.button("Reset", type="primary")
    if st.button("Kelompok 10"):
        st.write("Adinda Nazzala Siregar")
        st.write("Auliya kayla Putriandri")
        st.write("Muhammad Raynanda Hakim")
        st.write("Nur Ashima Wati")
        st.write("Trista Bintang Cendikia")

#horizontal menu
if test == "About Noble Gas👨‍🔬":
    from streamlit_option_menu import option_menu
    selected = option_menu(
    menu_title=None,
    options=["Gas Mulia","Penemu Gas Mulia","Keberadaan Gas Mulia"],
    orientation="horizontal",
)
    #Info
    if selected == "Gas Mulia":
        st.image('Identifikasi.png')
        st.title(":blue[Apa Itu Gas Mulia?]")
        st.markdown('<hr>', unsafe_allow_html=True)
        st.image('OIP.jpg')
        st.write('''
                 Dalam tabel periodik, gas mulia merupakan patokan kestabilan. 
                 Gas mulia merupakan unsur golongan 18 atau VIIIA, yang disebut
                 juga dengan golongan helium atau neon dan golongan aerogen.
                 Nomor atom gas mulia adalah 18 yang merupakan unsur yang sangat 
                 stabil. Inilah yang menyebabkan reaksi gas mulia menjadi sangat
                 sulit. Kestabilannya ini menurut Gilbert Newton Lewis, ahli kimia
                 dari Amerika, disebabkan karena konfigurasi elektron gas mulia yang 
                 bersifat penuh. Konfigurasi ini disebut sebagai oktet, khusus untuk
                 Helium disebut konfigurasi duplet. Energi ionisasi gas mulia sangat
                 besar dan afinitas elektronnya sangat rendah. Argon merupakan unsur
                 pertama gas muliayang ditemukan oleh ahli kimia asal Inggris bernama 
                 Sir William Ramsey. Kemudian di tahun 1962, seorang ahli kimia
                 asal Kanada bernama Neil Bartlett membuat senyawa gas mulia yang
                 dinamakan Xenon. Sejak saat itu, senyawa gas mulia 
                 yang lain pun dibuat.
                 ''')
    if selected == "Penemu Gas Mulia":
        st.image('Identifikasi.png')
        st.title(":blue[Penemu Gas Mulia]")
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write('''
                Penemuan gas mulia melibatkan beberapa ilmuwan, tetapi yang paling 
                terkenal adalah William Ramsay. Dia menemukan gas mulia neon, argon, 
                kripton, dan xenon pada akhir abad ke-19. Gas-gas ini disebut "mulia" 
                karena mereka sangat tidak reaktif secara kimia. Ramsay menggunakan 
                pemurnian air raksa untuk mengekstraksi gas-gas ini dari udara, yang 
                merupakan langkah penting dalam penelitian kimianya.
                 ''')
        st.image('220px-William_Ramsay.jpg', width=200)
        st.write('''
                 Ramsay memulai studinya di kota asalnya Glasgow dan menyelesaikan
                 gelar doktor di bidang kimia di Tübingen, dengan fokus pada kimia
                 organik. Sekembalinya ke Inggris Raya dan penunjukannya pada jabatan 
                 kademis di Universitas Bristol dan kemudian di University College
                 London, ia menjadi terkenal karena daya cipta dan ketelitiannya dalam
                 teknik eksperimennya, terutama metodenya dalam menentukan berat molekul
                 zat dalam keadaan cair.
                 ''')
    if selected == "Keberadaan Gas Mulia":
        st.image('Identifikasi.png')
        st.title(":blue[Keberadaan Gas Mulia]")
        st.markdown('<hr>', unsafe_allow_html=True)
        st.image('maxresdefault.jpg', width=500)
        st.write('''
                Gas Mulia terdapat dalam atmosfer bumi, untuk Helium terdapat di luar
                atmosfer. Helium dapat terbentuk dari peluruhan zat radioaktif uranium
                dan thorium. Semua unsur - unsur gas mulia terdiri dari atom -atom yang
                berdiri sendiri. Unsur gas mulia yang terbanyak di alam semesta adalah
                Helium (banyak terdapat di bintang) yang merupakan bahan bakar dari
                matahari. Radon amat sedikit jumlahnya di atmosfer atau udara. Dan
                sekalipun ditemukan akan cepat berubah menjadi unsur lain, karena
                radon bersifat radio aktif. Dan karena jumlahnya yang sangat sedikit
                pula radon disebut juga sebagi gas jarang.
                ''')



#Halaman Identifikasi
if test == "Noble Gas Identification🔬":
    st.image('Identifikasi.png')
    option = st.selectbox(
   "Masukan Nama Atom Gas Mulia",
   ("He", "Ne", "Ar","Kr","Xe","Rn"),
   index=None,
   placeholder="Atom Gas Mulia",

)
    if option == "He":
        st.image('200.gif', caption='Atom Helium', width=500)
        st.text('''
                Lambang : He
                Nama : Helium
                Nomor Atom : 2
                Massa Atom : 4,0026
                Jumlah Elektron : 2
                Junlah Proton : 2
                Jumlah Neutron : 2
                Jari-jari Atom (PM) : 99
                Tampilan : Tidak Berwarna
                Fase : Gas
                Kegunaan : Gas Pengisi Balon Udara
                ''')
    elif option == "Ne":
        st.image('giphy-11.gif', caption="Atom Neon",width=500)
        st.text('''
                 Lambang : Ne
                 Nama : Neon
                 Nomor Atom : 10
                 Massa Atom : 20,1800
                 Jumlah Elektron : 10
                 Jumlah Proton : 10
                 Jumlah Neutron : 10
                 Jari-jari Atom (PM) : 160
                 Tampilan : Tak Berwarna
                 Fase : Gas
                 Kegunaan : Pengisi Lampu Neon
                 ''')
    elif option == "Ar":
        st.image('giphy-downsized-large.gif', caption="Atom Argon")
        st.text('''
                 Lambang : Ar
                 Nama : Argon
                 Nomor Atom : 18
                 Massa Atom : 39,9478
                 Jumlah Elektron : 18
                 Jumlah Proton : 18
                 Jumlah Neutron : 22
                 Jari-jari Atom (PM) : 192
                 Tampilan : Tak Berwarna 
                 Fase : Gas
                 Kegunaan : Gas Pengisi Lampu Pijar
                 ''')
    elif option == "Kr":
        st.image('200w.gif', caption="Atom Kripton", width=500)
        st.text('''
                 Lambang : Kr
                 Nama : Kripton 
                 Nomor Atom : 36 
                 Massa Atom : 83,7980
                 Jumlah Elektron : 36
                 Jumlah Proton : 36
                 Jumlah Neutron : 48
                 Jari-jari Atom (PM) : 197
                 Tampilan : Tak Berwarna
                 Fase : Gas
                 Kegunaan : Lampu Kilat Untuk Fotografi
                 ''')
    elif option == "Xe":
        st.image('giphy (1).gif', caption="Atom Xenon")
        st.text('''
                 Lambang : Xe
                 Nama : Xenon
                 Nomor Atom : 54
                 Massa Atom : 131.2928
                 Jumlah Elektron : 54
                 Jumlah Proton : 54
                 Jumlah Neutron : 77
                 Jari-jari Atom (PM) : 271
                 Tampilan : Tak Berwarna
                 Fase : Gas
                 Kegunaan : Pembuatan Lampu Untuk Bakteria (Pembunuh Bakteri)
                 ''')
    elif option == "Rn":
        st.image('giphy.gif', caption="Atom Radon")
        st.text('''
                 Lambang : Rn
                 Nama : Radon
                 Nomor Atom : 86
                 Massa Atom : 222.0
                 Jumlah Elektron : 86
                 Jumlah Proton : 86
                 Jumlah Neutron : 136
                 Jari-jari Atom (PM) : 240
                 Tampilan : Tak Berwarna 
                 Fase : Gas
                 Kegunaan : Radioterapi Kanker
                 ''')