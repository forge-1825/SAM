#!/usr/bin/env python3
"""
SAM Setup Wizard UI
==================

Streamlit-based setup wizard for first-time SAM users.
Guides users through master password creation, SAM Pro activation,
and basic onboarding.
"""

import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

def show_setup_wizard():
    """Display the setup wizard interface."""
    try:
        from utils.first_time_setup import get_first_time_setup_manager
        setup_manager = get_first_time_setup_manager()
        
        # Get setup progress
        progress = setup_manager.get_setup_progress()
        next_step = progress['next_step']
        
        # Header
        st.markdown("# 🚀 Welcome to SAM!")
        st.markdown("### Let's get you set up in just a few steps")
        
        # Progress bar
        progress_bar = st.progress(progress['progress_percent'] / 100)
        st.markdown(f"**Setup Progress:** {progress['completed_steps']}/{progress['total_steps']} steps complete")
        
        st.divider()
        
        # Show appropriate setup step
        if next_step == 'master_password':
            show_master_password_setup(setup_manager)
        elif next_step == 'sam_pro_activation':
            show_sam_pro_activation(setup_manager)
        elif next_step == 'onboarding':
            show_onboarding_tour(setup_manager)
        else:
            show_setup_complete()
            
    except Exception as e:
        st.error(f"Setup wizard error: {e}")
        st.markdown("### 🔧 Manual Setup")
        st.markdown("If you're seeing this error, you can set up SAM manually:")
        st.markdown("1. Create your master password in the Security section")
        st.markdown("2. Enter your SAM Pro activation key")
        st.markdown("3. Start using SAM!")

def show_master_password_setup(setup_manager):
    """Show master password creation step."""
    st.markdown("## 🔐 Step 1: Create Master Password")
    st.markdown("""
    Your master password protects all SAM data with enterprise-grade encryption.
    
    **Important:**
    - Choose a strong, memorable password
    - This password encrypts all your conversations and data
    - You'll need this password every time you start SAM
    """)
    
    with st.form("master_password_form"):
        password = st.text_input("Master Password", type="password", 
                                help="Choose a strong password (8+ characters)")
        confirm_password = st.text_input("Confirm Password", type="password")
        
        if st.form_submit_button("Create Master Password", type="primary"):
            if not password:
                st.error("Please enter a password")
            elif len(password) < 8:
                st.error("Password must be at least 8 characters")
            elif password != confirm_password:
                st.error("Passwords don't match")
            else:
                # Create master password
                if create_master_password(password):
                    setup_manager.update_setup_status('master_password_created', True)
                    st.success("✅ Master password created successfully!")
                    st.rerun()
                else:
                    st.error("Failed to create master password. Please try again.")

def show_sam_pro_activation(setup_manager):
    """Show SAM Pro activation step."""
    st.markdown("## 🔑 Step 2: Activate SAM Pro")
    
    # Get the SAM Pro key
    sam_pro_key = setup_manager.get_sam_pro_key()
    
    if sam_pro_key:
        st.markdown("### Your SAM Pro Activation Key:")
        st.code(sam_pro_key, language=None)
        st.markdown("**💾 Important: Save this key!** You can use it to activate SAM Pro on other devices.")
        
        st.markdown("""
        ### 🎉 SAM Pro Features Included:
        - 🧠 **Cognitive Distillation Engine** - Learn from every interaction
        - 🧠 **TPV Active Reasoning Control** - Advanced reasoning capabilities
        - 📚 **MEMOIR Lifelong Learning** - Persistent memory across sessions
        - 🎨 **Dream Canvas Visualization** - Interactive memory landscapes
        - 🤖 **Cognitive Automation** - Autonomous task execution
        - 📊 **Advanced Analytics** - Deep insights and performance metrics
        """)
        
        if st.button("✅ Activate SAM Pro Features", type="primary"):
            # Activate SAM Pro
            if activate_sam_pro(sam_pro_key):
                setup_manager.update_setup_status('sam_pro_activated', True)
                st.success("🎉 SAM Pro activated successfully!")
                st.rerun()
            else:
                st.error("Failed to activate SAM Pro. Please try again.")
    else:
        st.warning("No SAM Pro key found. Please run setup again.")
        if st.button("🔄 Restart Setup"):
            st.rerun()

def show_onboarding_tour(setup_manager):
    """Show onboarding tour step."""
    st.markdown("## 🎓 Step 3: Welcome Tour")
    st.markdown("### You're almost ready! Let's quickly show you around SAM.")
    
    # Quick feature overview
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 💬 Chat Interface
        - Natural conversation with SAM
        - Upload documents for analysis
        - Ask questions about your data
        - Get intelligent insights
        """)
        
        st.markdown("""
        ### 🧠 Memory System
        - SAM remembers your conversations
        - Learns your preferences
        - Builds knowledge over time
        - Connects related information
        """)
    
    with col2:
        st.markdown("""
        ### 🎨 Dream Canvas
        - Visualize your memory landscape
        - Explore knowledge connections
        - Discover insights and patterns
        - Interactive memory exploration
        """)
        
        st.markdown("""
        ### 🔧 Advanced Features
        - Cognitive Automation
        - Document processing
        - Web research capabilities
        - Custom workflows
        """)
    
    st.markdown("### 🚀 Ready to start using SAM?")
    
    if st.button("🎉 Complete Setup & Start Using SAM!", type="primary"):
        setup_manager.update_setup_status('onboarding_completed', True)
        st.success("✅ Setup complete! Welcome to SAM!")
        st.rerun()

def show_setup_complete():
    """Show setup completion screen."""
    st.markdown("# 🎉 Setup Complete!")
    st.markdown("### Welcome to SAM - You're all set!")
    
    st.success("✅ All setup steps completed successfully")
    
    st.markdown("""
    ### 🚀 What you can do now:
    - Start chatting with SAM using the interface below
    - Upload documents to build your knowledge base
    - Explore the Memory Control Center
    - Try the Dream Canvas visualization
    - Access all SAM Pro features
    """)
    
    st.markdown("### 💡 Quick Tips:")
    st.markdown("- Use the sidebar to access different features")
    st.markdown("- Upload PDFs, documents, or text files for analysis")
    st.markdown("- Ask SAM questions about your uploaded content")
    st.markdown("- Explore the Memory section to see how SAM learns")
    
    if st.button("🚀 Start Using SAM", type="primary"):
        # Redirect to main chat interface
        st.switch_page("secure_streamlit_app.py")

def create_master_password(password: str) -> bool:
    """Create master password for encryption."""
    try:
        from security.crypto_utils import CryptoManager
        crypto_manager = CryptoManager()
        
        # Initialize encryption with the password
        success = crypto_manager.initialize_encryption(password)
        return success
        
    except Exception as e:
        st.error(f"Error creating master password: {e}")
        return False

def activate_sam_pro(activation_key: str) -> bool:
    """Activate SAM Pro features."""
    try:
        # The key should already be in the keystore from setup
        # Just need to mark it as activated in the entitlements
        from pathlib import Path
        import json
        
        entitlements_file = Path("security/entitlements.json")
        if entitlements_file.exists():
            with open(entitlements_file, 'r') as f:
                entitlements = json.load(f)
            
            # Mark SAM Pro as activated
            entitlements["sam_pro_keys"][activation_key] = {
                "activated": True,
                "activation_date": "2025-01-01T00:00:00",
                "features": [
                    "tpv_active_reasoning",
                    "enhanced_slp_learning", 
                    "memoir_lifelong_learning",
                    "dream_canvas",
                    "cognitive_distillation",
                    "cognitive_automation"
                ]
            }
            
            with open(entitlements_file, 'w') as f:
                json.dump(entitlements, f, indent=2)
            
            return True
        
        return False
        
    except Exception as e:
        st.error(f"Error activating SAM Pro: {e}")
        return False

if __name__ == "__main__":
    show_setup_wizard()
