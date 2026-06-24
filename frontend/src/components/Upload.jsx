import { useState, useCallback } from "react"
import { useDropzone } from "react-dropzone"
import axios from "axios"
import { Upload as UploadIcon, Image } from "lucide-react"

const API_URL = "http://localhost:8000"

function Upload({ setResult, setLoading, setPreview, loading }) {
  const [error, setError] = useState(null)

  const onDrop = useCallback(async (acceptedFiles) => {
    const file = acceptedFiles[0]
    if (!file) return

    // Show preview
    const previewUrl = URL.createObjectURL(file)
    setPreview(previewUrl)
    setResult(null)
    setError(null)
    setLoading(true)

    try {
      const formData = new FormData()
      formData.append("file", file)

      const response = await axios.post(
        `${API_URL}/predict?include_gradcam=true`,
        formData,
        { headers: { "Content-Type": "multipart/form-data" } }
      )
      setResult(response.data)
    } catch (err) {
      setError(err.response?.data?.detail || "Something went wrong!")
    } finally {
      setLoading(false)
    }
  }, [setResult, setLoading, setPreview])

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: { "image/*": [".jpg", ".jpeg", ".png", ".webp"] },
    maxFiles: 1,
    disabled: loading,
  })

  return (
    <div className="upload-section">
      <div
        {...getRootProps()}
        className={`dropzone ${isDragActive ? "active" : ""} ${loading ? "disabled" : ""}`}
      >
        <input {...getInputProps()} />
        <div className="dropzone-content">
          {isDragActive ? (
            <Image size={48} color="#22c55e" />
          ) : (
            <UploadIcon size={48} color="#888" />
          )}
          <p className="dropzone-text">
            {isDragActive
              ? "Drop the image here..."
              : "Drag & drop a leaf image, or click to select"}
          </p>
          <p className="dropzone-hint">Supports JPG, PNG, WEBP — max 10MB</p>
        </div>
      </div>

      {error && (
        <div className="error-box">
          ⚠️ {error}
        </div>
      )}
    </div>
  )
}

export default Upload