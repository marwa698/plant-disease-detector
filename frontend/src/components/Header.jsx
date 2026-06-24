import { Leaf } from "lucide-react"

function Header() {
  return (
    <header className="header">
      <div className="header-content">
        <div className="logo">
          <Leaf size={28} color="#22c55e" />
          <span className="logo-text">Plant Disease Detector</span>
        </div>
        <p className="header-subtitle">
          Upload a leaf image to detect plant diseases using AI
        </p>
      </div>
    </header>
  )
}

export default Header