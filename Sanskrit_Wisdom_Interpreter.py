import pyttsx3
import os
import winsound
import time

# ===============================
# Text-to-Speech Setup
# ===============================
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 120)
engine.setProperty('volume', 1.0)

# ===============================
# Sanskrit Shlokas Database (20)
# ===============================
shlokas = {
    "1": {"shloka": "धर्मो रक्षति रक्षितः", "meaning": "Dharma protects those who protect dharma."},
    "2": {"shloka": "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन", "meaning": "You have the right to action not to results."},
    "3": {"shloka": "सत्यं ब्रूयात् प्रियं ब्रूयात्", "meaning": "Speak the truth pleasantly."},
    "4": {"shloka": "अहिंसा परमो धर्मः", "meaning": "Non violence is the highest duty."},
    "5": {"shloka": "न आत्मानमवसादयेत्", "meaning": "Never degrade yourself."},
    "6": {"shloka": "क्रोधाद्भवति सम्मोहः", "meaning": "From anger comes confusion."},
    "7": {"shloka": "मातृदेवो भवः", "meaning": "Mother is divine."},
    "8": {"shloka": "अति सर्वत्र वर्जयेत्", "meaning": "Avoid excess everywhere."},
    "9": {"shloka": "विद्या ददाति विनयं", "meaning": "Knowledge gives humility."},
    "10": {"shloka": "परित्यजेदर्थकामौ यौ स्यातां धर्मवर्जितौ", "meaning": "Abandon wealth if it opposes righteousness."},
    "11": {"shloka": "न हि ज्ञानेन सदृशं पवित्रमिह विद्यते", "meaning": "Nothing is as purifying as true knowledge."},
    "12": {"shloka": "उद्धरेदात्मनाऽत्मानं नात्मानमवसादयेत्", "meaning": "Uplift yourself by your own efforts."},
    "13": {"shloka": "सन्तोषः परमं सुखम्", "meaning": "Contentment is the highest happiness."},
    "14": {"shloka": "धैर्यं सर्वत्र साधनम्", "meaning": "Patience is the solution everywhere."},
    "15": {"shloka": "सर्वं परवशं दुःखं सर्वमात्मवशं सुखम्", "meaning": "Self control brings happiness."},
    "16": {"shloka": "अयं निजः परो वेति गणना लघुचेतसाम्", "meaning": "The world is one family."},
    "17": {"shloka": "न विद्या विवादाय धनं मदाय", "meaning": "Knowledge is not for argument."},
    "18": {"shloka": "कालेन सर्वं प्राप्यते", "meaning": "Everything happens in its own time."},
    "19": {"shloka": "न कर्मणा न प्रजया धनेन", "meaning": "Greatness comes through sacrifice."},
    "20": {"shloka": "सत्यं एव जयते", "meaning": "Truth alone triumphs."}
}

# ===============================
# Program Start
# ===============================
print("\n===== Sanskrit Wisdom Interpreter =====\n")

for k in shlokas:
    print(f"{k}. {shlokas[k]['shloka']}")

choice = input("\nEnter the number of the shloka: ").strip()

if choice in shlokas:
    meaning = shlokas[choice]["meaning"]
    shloka = shlokas[choice]["shloka"]

    print("\nShloka:", shloka)
    print("Meaning:", meaning)

    # 🔊 Generate audio file
    audio_file = "meaning.wav"
    engine.save_to_file(meaning, audio_file)
    engine.runAndWait()

    time.sleep(0.5)

    # 🔊 Play audio file (GUARANTEED)
    winsound.PlaySound(audio_file, winsound.SND_FILENAME)

else:
    print("Invalid choice")