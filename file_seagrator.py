import os
location=raw_input("Enter the Location: ")
print location
video=['.mpg','.mp4','.mpeg','.avi','.mov','.qt','.wmv','flv']
audio=['.mp3','.wma','.waw']
images=['.gif','.jpg','jpeg','.jpe','.bmp','.png','.tif']
pdf=['.pdf']
exe=['.exe']
compressed=['.zip','.rar','.tar','.gz','.tgz']
flash=['.swf']
web=['.html','.php']
files=[x[2] for x in os.walk(location)]
folder=[x[0] for x in os.walk(location)]
dirvideo=location+'/'+'file_seagretor'+'/Video/'
diraudio=location+'/'+'file_seagretor'+'/Audio/'
dirimages=location+'/'+'file_seagretor'+'/Images/'
dirpdf=location+'/'+'file_seagretor'+'/PDF/'
direxe=location+'/'+'file_seagretor'+'/Programs/'
dircompress=location+'/'+'file_seagretor'+'/Compress/'
dirflash=location+'/'+'file_seagretor'+'/Flash/'
dirweb=location+'/'+'file_seagretor'+'/Webpage/'
dirun=location+'/'+'file_seagretor'+'/Unspecified/'
#if not os.path.exists(dirvideo):
#    os.makedirs(dirvideo)
#    os.makedirs(diraudio)
#    os.makedirs(dirimages)
#    os.makedirs(dirpdf)
#    os.makedirs(direxe)
#    os.makedirs(dircompress)
#    os.makedirs(dirflash)
#    os.makedirs(dirweb)
#    os.makedirs(dirun)

for f in range(0,len(folder)):
    for e in files[f]:
        print folder[f]+'/'+e
        done=False
        el=e.lower()
        for i in video:
            if el.find(i)!=-1 and done==False:
                if not os.path.exists(dirvideo):
                    os.makedirs(dirvideo)
                os.rename(folder[f]+"/"+e, dirvideo+e)
                done=True
        for i in audio:
            if el.find(i)!=-1 and done==False:
                if not os.path.exists(diraudio):
                    os.makedirs(diraudio)
                os.rename(folder[f]+"/"+e, diraudio+e)
                done=True
        for i in images:
            if el.find(i)!=-1 and done==False:
                if not os.path.exists(dirimages):
                    os.makedirs(dirimages)
                os.rename(folder[f]+"/"+e, dirimages+e)
                done=True
        for i in pdf:
            if el.find(i)!=-1 and done==False:
                if not os.path.exists(dirpdf):
                    os.makedirs(dirpdf)
                os.rename(folder[f]+"/"+e, dirpdf+e)
                done=True
        for i in exe:
            if el.find(i)!=-1 and done==False:
                if not os.path.exists(direxe):
                    os.makedirs(direxe)
                os.rename(folder[f]+"/"+e, direxe+e)
                done=True
        for i in compressed:
            if el.find(i)!=-1 and done==False:
                if not os.path.exists(dircompress):
                    os.makedirs(dircompress)
                os.rename(folder[f]+"/"+e, dircompress+e)
                done=True
        for i in flash:
            if el.find(i)!=-1 and done==False:
                if not os.path.exists(dirflash):
                    os.makedirs(dirflash)
                os.rename(folder[f]+"/"+e, dirflash+e)
                done=True
        for i in web:
            if el.find(i)!=-1 and done==False:
                if not os.path.exists(dirweb):
                    os.makedirs(dirweb)
                os.rename(folder[f]+"/"+e, dirweb+e)
                done=True
        if done==False:
            if not os.path.exists(dirun):
                    os.makedirs(dirun)
            os.rename(folder[f]+"/"+e, dirun+e)        
        
    
