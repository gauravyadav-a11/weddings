import os, uuid
from flask import Flask, Response, render_template, redirect, url_for, request, session, escape
from flaskext.mysql import MySQL

app = Flask(__name__, static_url_path='/static')
mysql = MySQL()
UPLOAD_FOLDER = '/Users/apple/Desktop/login/media/uploadphotos'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'hotaaa123'
app.config['MYSQL_DATABASE_DB'] = 'wedding'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        return open(src).read()
    except IOError as exc:
        return str(exc)
#homepage
@app.route('/')
def home():
    if 'username' in session:
        return render_template("index.html", username=session['username'])
    return render_template("index.html", username=None)

#register as couples
@app.route('/register_c', methods=['GET','POST'])
def register_c():
    error=None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        couplename = request.form['couplename']
        couplephone =request.form['couplephone']
        coupleemail = request.form['coupleemail']
        coupleinfo = request.form['coupleinfo']
        cid = request.form['cid']
        cursor.execute("SELECT username FROM couples WHERE username = '%s'" % (username))
        findaccounts = cursor.fetchone()
        if findaccounts:
            error = 'Existed username. Try a new one.'
            return render_template('register_c.html', error = error)
        else: 
            cursor.execute("insert into couples (username,password,couplename,coupleemail,couplephone,coupleinfo) values ('%s','%s','%s','%s','%s','%s')" % (username,password, couplename, coupleemail, couplephone, coupleinfo))
            conn.commit()
            session['username'] = request.form['username']
            session['cid'] = cid
            return redirect(url_for('home'))
    return render_template('register_c.html', error=error)

#register as photographers
@app.route('/register_p', methods=['GET','POST'])
def register_p():
    cursor.execute("SELECT * FROM destinations")
    rows = cursor.fetchall()
    destinations = []
    for row in rows:
        b = {}
        b['id'] = row[0]
        b['destination'] = row[1]
        destinations.append(b)
    return render_template('register_p.html', destinations=destinations)

#insert register_p info into database (photographers)
@app.route('/register_validate', methods=['GET','POST'])
def register_validate():
    error=None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        photographername = request.form['photographername']
        photographeremail = request.form['photographeremail']
        photographerphone = request.form['photographerphone']
        photographerinfo = request.form['photographerinfo']
        destination = request.form['destination']
        pid = request.form['pid']
        sql = "SELECT username FROM photographers WHERE username = '%s'" % (username)
        cursor.execute(sql)
        conn.commit()
        findaccounts = cursor.fetchone()
        if findaccounts:
            error = 'Existed username. Try a new one.'
            return render_template('register_p.html', error = error)
        else: 
            cursor.execute("insert into photographers (username,password,photographername, photographeremail, photographerphone, photographerinfo, dp_id) values ('%s','%s', '%s','%s','%s','%s', %s)" % (username,password,photographername, photographeremail, photographerphone, photographerinfo, destination))
            conn.commit()
            session['username'] = request.form['username']
            session['cid'] = cid
            return redirect(url_for('home'))
    return redirect(url_for('register_p'))

#login as couples
@app.route('/login_c', methods=['GET', 'POST'])
def login_c():
    error = None
    if request.method == 'POST': 
        username = request.form['username']
        password = request.form['password']
        cid= request.form['cid']
        cursor.execute("SELECT id, password FROM couples WHERE username = '%s'" % (username))
        findaccounts = cursor.fetchone()
        cid = findaccounts[0]
        rightpassword = findaccounts[1]
        if password != rightpassword:
            error = 'Invalid Password. Please try again.'
        else:
            session['username'] = request.form['username']
            session['cid'] = cid
            return redirect(url_for('home'))          
    return render_template('login_c.html', error=error)

#login as photographers
@app.route('/login_p', methods=['GET', 'POST'])
def login_p():
    error = None
    if request.method == 'POST': 
        username = request.form['username']
        password = request.form['password']
        pid=request.form['pid']
        cursor.execute("SELECT id, password FROM photographers WHERE username = '%s'" % (username))
        findaccounts = cursor.fetchone()
        pid = findaccounts[0]
        rightpassword = findaccounts[1]
        if password != rightpassword:
            error = 'Invalid Password. Please try again.'
        else:
            session['username'] = request.form['username']
            session['pid'] = pid
            return redirect(url_for('home'))
    return render_template('login_p.html', error=error)

#logout for both couples and photographers
@app.route('/logout')
def logout():
    if session.has_key('pid'):
        if session.has_key('aid'):
            del session['aid']
        session.pop('username', None)
        del session['pid']
        return redirect(url_for('home'))
    else:
        session.pop('username', None)
        del session['cid']
        return redirect(url_for('home'))

#create my albums(for photographers)
@app.route('/createalbums', methods=['GET','POST'])
def albums():
    error=None
    if 'pid' in session:
        if request.method == 'POST':
            albumname = request.form['albumname']
            information = request.form['information']
            pid = session['pid']
            cursor.execute("SELECT albumname FROM albums WHERE albumname = '%s'" % (albumname))
            findalbums = cursor.fetchone()
            print("HELLO %s" % str(findalbums))
            if findalbums != None:
                error = 'Existed albumname. Try a new one.'
            else:
                cursor.execute("insert into albums (albumname,information, pa_id) values ('%s','%s',%s)" % (albumname,information,pid))
                conn.commit()
            return redirect(url_for('showalbums'))
        return render_template('albums.html', error=error)
    return render_template('hintp.html')

# show self all albums (for phtographers)
@app.route('/showalbums')
def showalbums():
    if 'pid' in session:
        cursor.execute("SELECT * FROM albums WHERE pa_id = %s" % session['pid'])
        rows = cursor.fetchall()
        albums = []
        for row in rows:
            b = {}
            b['id'] = row[0]
            b['albumname'] = row[2]
            b['information']=row[3]
            b['cover']=row[4]
            albums.append(b)
        return render_template('albums.html', albums=albums)
    return render_template('hintp.html')

#delete my albums(for photographers)
@app.route('/albums/<int:aid>/delete', methods=['GET'])
def deletealbums(aid):
    if 'pid' in session:
        album_id = aid
        delete = "DELETE FROM albums WHERE id ='%s'" % album_id
        cursor.execute(delete)
        conn.commit()
        return redirect(url_for('showalbums'))
    return render_template('hintp.html')

#rename my albums (for photographers) 
@app.route('/albums/edit', methods=['GET', 'POST'])
def renamealbums():
    if 'pid' in session:
        aid = request.form['aid']
        newname = request.form['album_newname']
        rename="UPDATE albums SET albumname = '%s' WHERE id = %s" % (newname, aid)
        cursor.execute(rename)
        conn.commit()
        return redirect(url_for('showalbums'))
    return render_template('hintp.html')

#albums gallery for all
@app.route('/gallery', methods=['GET','POST'])
def gallery():
    cursor.execute("SELECT albums.albumname, albums.cover, photographers.photographername, albums.id FROM photographers INNER JOIN albums ON albums.pa_id = photographers.id")
    rows = cursor.fetchall()
    albums = []
    for row in rows:
        b = {}
        b['albumname'] = row[0]
        b['cover'] = row[1]
        b['photographername'] = row[2]
        b['id']=row[3]
        albums.append(b)
    return render_template('gallery.html', albums=albums)
    

@app.route('/process_albumdetail',methods=['GET','POST'])
def process_albumdetail():
    if request.method == 'POST':
        aid = request.form['aid']
        session['aid'] = aid
        return redirect('/albumdetail/'+ session['aid'])
    return render_template('gallery.html')

# view photos in selected albums for all
@app.route('/albumdetail/<int:aid>')
def albumdetail(aid):
    cursor.execute("SELECT albumname, information FROM albums WHERE id = %s" % aid)
    albumdetail=cursor.fetchone()
    albumname=albumdetail[0]
    albuminformation=albumdetail[1]

    cursor.execute("SELECT  path, photoname, photoinformation, id FROM photos WHERE ap_id = %s" % aid)
    rows = cursor.fetchall()
    photos = []
    for row in rows:
        b={}
        b['path'] = row[0]
        b['photoname']=row[1]
        b['photoinformation']=row[2]
        b['id']=row[3] 
        photos.append(b)
    return render_template('albumdetail.html', photos=photos, albumdetail=albumdetail)

#define img
@app.route('/img/<path:path>')
def get_resource(path):  
    complete_path = os.path.join(app.config['UPLOAD_FOLDER'], path)
    ext = os.path.splitext(path)[1]
    content = get_file(complete_path)
    return Response(content, mimetype="image/jpeg")

#view albums selection bar in upload photos page
@app.route('/photos_albumsform', methods=['GET','POST'])
def photos_albumsform():
    if 'pid' in session:
        cursor.execute("SELECT * FROM albums WHERE pa_id = %s" % session['pid'])
        rows = cursor.fetchall()
        albums = []
        for row in rows:
            b = {}
            b['id'] = row[0]
            b['albumname'] = row[2]
            albums.append(b)
        return render_template('upload.html', albums = albums)
    return render_template("hintp.html")

#upload photos and insert data into sql
@app.route('/uploadphotos', methods=['GET', 'POST'])
def uploadphotos():
    if request.method == 'POST':
        aid = request.form['aid']
        file = request.files['file']
        extension = os.path.splitext(file.filename)[1]
        f_name = str(uuid.uuid4()) + extension
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
        cursor.execute("insert into photos (path,ap_id) values ('%s',%s)" % (f_name,aid))
        conn.commit()
        return redirect('/albumdetail/'+aid)
    return render_template("upload.html", sucess=False,f_name=f_name)


#home>photographers>view all photographers
@app.route('/photographerlist')
def photographerlist():
    cursor.execute("SELECT destinations.city, photographers.portrait, photographers.photographername, photographers.id FROM photographers INNER JOIN destinations ON photographers.dp_id = destinations.id")
    rows = cursor.fetchall()
    photographerlists = []
    for row in rows:
        b = {}
        b['city'] = row[0]
        b['portrait'] = row[1]
        b['photographername'] = row[2]
        b['id']=row[3]
        photographerlists.append(b)
    return render_template('photographerlist.html', photographerlists=photographerlists)

#process of view portfolio of one photographer
@app.route('/process_viewportfolio', methods=['GET','POST'])
def process_viewportfolio():
    if request.method == 'POST':
        portfoliopid = request.form['portfoliopid']
        session['portfoliopid'] = portfoliopid
        return redirect('/portfolio/'+ session['portfoliopid'])
    return redirect('/photographerlists')

# page of view portfolio of one photographer
@app.route('/portfolio/<int:portfoliopid>')
def portfolio(portfoliopid):
    cursor.execute("SELECT * FROM photographers WHERE id = %s" % session['portfoliopid'])
    rows = cursor.fetchall()
    portfolios = []
    for row in rows:
        b = {}
        b['dp_id']=row[1]
        b['portrait'] = row[4]
        b['photographername']=row[5]
        b['photographeremail']=row[6]
        b['photographerphone'] =row[7]
        b['photographerinfo'] = row[8]
        portfolios.append(b)

    cursor.execute("SELECT * FROM albums WHERE pa_id = %s" % session['portfoliopid'])
    albumlists = cursor.fetchall()
    albums = []
    for albumlist in albumlists:
        b = {}
        b['id']=albumlist[0]
        b['albumname']= albumlist[2]
        b['infomation'] = albumlist[3]
        b['cover']=albumlist[4]
        albums.append(b)
        
    cursor.execute("SELECT destinations.city, photographers.dp_id FROM destinations INNER JOIN photographers ON photographers.dp_id = destinations.id WHERE photographers.id = %s" % session['portfoliopid'])
    place = cursor.fetchone()
    city = place[0]
    dpid = place[1]
    print (city)

    cursor.execute("SELECT * FROM photographers WHERE dp_id=%s" % dpid)
    others = cursor.fetchall()
    portfolioothers = []
    for other in others:
        b = {}
        b['photographername'] = other[5]
        b['id'] = other[0]
        b['portrait']= other[4]
        portfolioothers.append(b)
    return render_template('portfolio.html', portfolioothers = portfolioothers , portfolios = portfolios, city=city, dpid=dpid, albums=albums)

#plan step1 select destination (for couples)        
@app.route('/process_step1', methods=['GET','POST'])
def process_step1():
    if 'cid' in session:
        cursor.execute("SELECT * FROM destinations")
        rows = cursor.fetchall()
        destinations = []
        for row in rows:
            b = {}
            b['id'] = row[0]
            b['destination'] = row[1]
            destinations.append(b)
        return render_template('plan_step1.html', destinations=destinations)
    else:
        return render_template('hintc.html')

#process plan_step1 to step2
@app.route('/plan_step1', methods=['GET','POST'])
def plan_step1():
    if request.method == 'POST':
        did = request.form['destination']
        session['did'] = did
        return redirect('/plan_step2/' + session['did'])
    return redirect(url_for('process_step1'))

#plan_step2 select photographer(for couples)
@app.route('/plan_step2/<int:did>')
def plan_step2(did):
    cursor.execute("SELECT * FROM photographers WHERE dp_id = %s" % session['did'])
    rows = cursor.fetchall()
    planphotographers = []
    for row in rows:
        b = {}
        b['id'] = row[0]
        b['portrait'] = row[4]
        b['photographername'] = row[5]
        b['photographerinfo'] = row[8]
        planphotographers.append(b)  
    cursor.execute("SELECT city FROM destinations WHERE id = %s" % session['did'])
    pland = cursor.fetchone()
    city = pland[0]
    return render_template('plan_step2.html', pland=pland, city=city, planphotographers=planphotographers)

#process plan_step2 to plan_step3
@app.route('/process_step2', methods=['GET','POST'])
def process_step2():
    if request.method == 'POST':
        choosepid = request.form['choosepid']
        session['choosepid'] = choosepid
        return redirect('plan_step3')
    return redirect('/plan_step2/'+ session['did'])

#plan_step 3 insert all info into sql
@app.route('/plan_step3', methods=['POST','GET'])
def plan_step3():
    cursor.execute("SELECT city FROM destinations WHERE id = %s" % session['did'])
    pland = cursor.fetchone()
    city = pland[0] 
    cursor.execute("SELECT photographername FROM photographers WHERE id = %s" % session['choosepid'])
    planp = cursor.fetchone()
    photographer = planp[0]
    if request.method == 'POST':
        did = session['did']
        choosepid = session['choosepid']
        cid = session['cid']
        orderdate = request.form['orderdate']
        orderrequirement = request.form['orderrequirement']
        cursor.execute("insert into orders (oc_id, op_id, od_id, orderdate, orderrequirement) values (%s, %s, %s ,'%s','%s')" % (cid, choosepid, did, orderdate, orderrequirement))
        conn.commit() 
        return redirect(url_for('home'))
    return render_template('plan_step3.html', city = city, photographer = photographer)

@app.route('/vieworder')
def vieworder():
    if 'pid' in session:
        return redirect(url_for('vieworderpid'))
    if 'cid' in session:
        return redirect(url_for('viewordercid'))
    return render_template('hint.html')

#review orderlist for photographers
@app.route('/vieworderpid')
def vieworderpid():
    cursor.execute("SELECT * FROM orders WHERE op_id=%s" % session['pid'])
    rows= cursor.fetchall()
    orderlists = []
    for row in rows:
        b={}
        b['id'] = row[0]
        b['orderdate'] = row[4]
        orderlists.append(b)
    return render_template('vieworderpid.html', orderlists=orderlists)

#process selected order to view order details
@app.route('/process_vieworderpid', methods=['GET','POST'])
def process_vieworderpid():
    if request.method == 'POST':
        oid = request.form['oid']
        session['oid'] = oid
        return redirect('/orderdetailspid/'+ session['oid'])

#orderdetails(for photographers)
@app.route('/orderdetailspid/<int:oid>', methods=['GET','POST'])
def orderdetailspid(oid):
    cursor.execute("SELECT couples.couplename, couples.coupleemail, couples.couplephone, couples.coupleinfo,orders.orderdate, orders.orderrequirement, orders.id FROM orders INNER JOIN couples ON orders.oc_id = couples.id WHERE orders.id = %s" % session['oid'])
    rows = cursor.fetchall()
    orderdetails = []
    for row in rows:
        b = {}
        b['couplename'] = row[0]
        b['coupleemail'] = row[1]
        b['couplephone'] = row[2]
        b['coupleinfo'] = row[3]
        b['orderdate'] = row[4]
        b['orderrequirement'] = row[5]
        b['id']=row[6]
        orderdetails.append(b)
    return render_template('orderdetailspid.html', orderdetails = orderdetails)

#review orderlist for couples
@app.route('/viewordercid')
def viewordercid():
    cursor.execute("SELECT * FROM orders WHERE oc_id=%s" % session['cid'])
    rows= cursor.fetchall()
    orderlists = []
    for row in rows:
        b={}
        b['id'] = row[0]
        b['orderdate'] = row[4]
        orderlists.append(b)
    return render_template('viewordercid.html', orderlists=orderlists)


#process selected order to view order details couples
@app.route('/process_viewordercid', methods=['GET','POST'])
def process_viewordercid():
    if request.method == 'POST':
        oid = request.form['oid']
        session['oid'] = oid
        return redirect('/orderdetailscid/'+ session['oid'])

#orderdetails(for couples)
@app.route('/orderdetailscid/<int:oid>', methods=['GET','POST'])
def orderdetailscid(oid):
    cursor.execute("SELECT photographers.photographername, photographers.photographeremail, photographers.photographerphone, photographers.photographerinfo,orders.orderdate, orders.orderrequirement, orders.id FROM orders INNER JOIN photographers ON orders.op_id = photographers.id WHERE orders.id = %s" % session['oid'])
    rows = cursor.fetchall()
    orderdetails = []
    for row in rows:
        b = {}
        b['photographername'] = row[0]
        b['photographeremail'] = row[1]
        b['photographerphone'] = row[2]
        b['photographerinfo'] = row[3]
        b['orderdate'] = row[4]
        b['orderrequirement'] = row[5]
        b['id']=row[6]
        orderdetails.append(b)
    cursor.execute("SELECT destinations.city FROM destinations INNER JOIN orders ON orders.od_id = destinations.id WHERE orders.id = %s" % session['oid'])
    destinationname = cursor.fetchone()
    city = destinationname[0]
    return render_template('orderdetailscid.html', orderdetails = orderdetails, destinationname=destinationname)

#destination page
@app.route('/destinations')
def destinations():
    cursor.execute("SELECT * FROM destinations")
    rows = cursor.fetchall()
    destinations = []
    for row in rows:
        b = {} 
        b['id'] = row[0]
        b['city'] = row[1]
        b['country']= row[2]
        b['dphoto1']=row[4]
        destinations.append(b)
    print (destinations)
    if request.method == 'POST':
        destinationid = destination['destinationid']
        session['destinationid']= destinationid
        return redirect('/albumdetail/'+ session['destinationid'])
    return render_template('destinations.html', destinations=destinations)

@app.route('/destinationdetail/<int:destinationid>')
def destinationdetail(destinationid):
    cursor.execute("SELECT * FROM destinations where id = %s" % destinationid)
    detail = cursor.fetchone()
    dcity = detail[1]
    dcountry = detail[2]
    dcustomhabit = detail[3]
    ddphoto1 = detail[4]
    ddphoto2 = detail[5]
    ddphoto3 = detail[6]
    ddphoto4 = detail[7]
    cursor.execute("SELECT * FROM photographers WHERE dp_id = %s" % destinationid)
    rows = cursor.fetchall()
    dphotographers =[]
    for row in rows:
        b = {} 
        b['id'] = row[0]
        b['photographername'] = row[5]
        b['portrait'] = row[4]
        dphotographers.append(b) 
    return render_template('destinationdetail.html', detail=detail, dphotographers=dphotographers) 


# photographer view self profile
@app.route('/profile')
def profile():
    if 'pid' in session:
        cursor.execute("SELECT * FROM photographers WHERE id = %s" % session['pid'])
        rows = cursor.fetchall()
        profilepids = []
        for row in rows:
            b = {}
            b['id']=row[0] 
            b['username'] = row[2]
            b['password'] = row[3]
            b['portrait'] = row[4]
            b['photographername']=row[5]
            b['photographeremail']=row[6]
            b['photographerphone'] =row[7]
            b['photographerinfo'] = row[8]
            profilepids.append(b)    
        cursor.execute("SELECT destinations.city, photographers.id FROM destinations INNER JOIN photographers ON photographers.dp_id = destinations.id WHERE photographers.id = %s" % session['pid'])
        profilecity = cursor.fetchone()
        city = profilecity[0]
        return render_template('profilepid.html', profilepids=profilepids, profilecity=profilecity)
    if 'cid' in session:
        cursor.execute("SELECT * FROM couples WHERE id = %s" % session['cid'])
        rows = cursor.fetchall()
        profilecids = []
        for row in rows:
            b = {} 
            b['username'] = row[1]
            b['password'] = row[2]
            b['portrait'] = row[3]
            b['couplename']=row[4]
            b['coupleemail']=row[5]
            b['couplephone'] =row[6]
            b['coupleinfo'] = row[7]
            profilecids.append(b)    
        return render_template('profilecid.html', profilecids=profilecids)
    return render_template('hint.html')




if __name__ == '__main__':
	app.run(host='0.0.0.0')

