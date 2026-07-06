# မြန်မာစာ Text-to-Speech (Myanmar TTS)

Flask + edge-tts ဖြင့် ရေးထားသော မြန်မာစာအသံဖတ် web app။

## Local Run
```bash
pip install -r requirements.txt
python app.py
```
ဖွင့်ရန်: http://localhost:5000

## Render မှာ Deploy လုပ်နည်း (Public Deploy)

1. ဒီ project folder (Myapp1) ကို GitHub repo အသစ်တစ်ခုအဖြစ် push လုပ်ပါ။
2. https://render.com ကို ဝင်ပြီး **New +** → **Web Service** ကိုနှိပ်ပါ။
3. သင့် GitHub repo ကို ချိတ်ဆက်ပါ (repo ကို public ဖြစ်စေချင်ရင် public လုပ်ထားပါ၊ Render account connect ရုံနဲ့လည်း private repo ကို သုံးလို့ရပါတယ်)။
4. Settings များ:
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free (စမ်းသပ်ဖို့)
5. **Create Web Service** ကိုနှိပ်လိုက်ရင် Render က build + deploy အလိုအလျောက်လုပ်ပေးပါလိမ့်မယ်။
6. Deploy ပြီးရင် `https://your-app-name.onrender.com` လိုမျိုး public URL တစ်ခု ရရှိပါလိမ့်မယ်။

`render.yaml` ဖိုင်ပါထည့်ပေးထားလို့၊ Render dashboard ထဲက **Blueprint** option သုံးရင်လည်း settings တွေကို auto-detect လုပ်ပေးပါလိမ့်မယ်။

### မှတ်ချက်
- Free plan မှာ app က idle ဖြစ်သွားရင် request အသစ်ဝင်လာချိန် (cold start) စာနည်းနည်း နှေးနိုင်ပါတယ်။
- `edge-tts` က Microsoft ရဲ့ online TTS service ကို အသုံးပြုတာဖြစ်လို့ Render server ကနေ internet ချိတ်ဆက်နိုင်ဖို့ လိုအပ်ပါတယ် (default အတိုင်း အလုပ်လုပ်ပါတယ်)။
- Voice အသစ်များ ထပ်ထည့်ချင်ရင် `app.py` ထဲက `VOICES` dictionary ထဲမှာ ထည့်ရုံပါပဲ။

## Project Structure
```
Myapp1/
├── app.py              # Flask backend
├── templates/
│   └── index.html      # UI (redesigned, Myanmar-themed)
├── requirements.txt
├── Procfile            # Render/gunicorn start command
└── render.yaml          # Render blueprint (optional one-click config)
```
