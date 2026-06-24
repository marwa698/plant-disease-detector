import { CheckCircle, AlertTriangle, XCircle, Clock, Leaf } from "lucide-react"

const SEVERITY_ICONS = {
  low   : <CheckCircle size={20} color="#22c55e" />,
  medium: <AlertTriangle size={20} color="#f97316" />,
  high  : <XCircle size={20} color="#ef4444" />,
}

function Result({ result, loading, preview }) {
  if (loading) {
    return (
      <div className="result-section">
        <div className="loading-card">
          <div className="spinner" />
          <p>Analyzing leaf image...</p>
        </div>
      </div>
    )
  }

  if (!result) return null

  const { top_prediction, all_predictions, disease_info, inference_time_ms, gradcam_image } = result

  return (
    <div className="result-section">

      {/* ── Top Row ── */}
      <div className="result-grid">

        {/* Image + Grad-CAM */}
        <div className="card image-card">
          <h3 className="card-title">
            <Leaf size={18} /> Leaf Analysis
          </h3>
          <div className="image-compare">
            {preview && (
              <div className="img-wrapper">
                <p className="img-label">Original</p>
                <img src={preview} alt="Original leaf" className="leaf-img" />
              </div>
            )}
            {gradcam_image && (
              <div className="img-wrapper">
                <p className="img-label">Grad-CAM</p>
                <img
                  src={`data:image/png;base64,${gradcam_image}`}
                  alt="Grad-CAM"
                  className="leaf-img"
                />
              </div>
            )}
          </div>
          <p className="inference-time">
            <Clock size={14} /> Inference: {inference_time_ms}ms
          </p>
        </div>

        {/* Diagnosis */}
        <div className="card diagnosis-card">
          <h3 className="card-title">Diagnosis Result</h3>

          <div
            className="diagnosis-badge"
            style={{ borderColor: disease_info.severity_color }}
          >
            <div className="diagnosis-header">
              {SEVERITY_ICONS[disease_info.severity]}
              <span className="disease-name">{disease_info.name}</span>
            </div>
            <p className="disease-plant">🌿 {disease_info.plant}</p>
            <p className="disease-desc">{disease_info.description}</p>
          </div>

          {/* Confidence Bar */}
          <div className="confidence-section">
            <div className="confidence-row">
              <span>Confidence</span>
              <span className="confidence-pct">
                {(top_prediction.confidence * 100).toFixed(1)}%
              </span>
            </div>
            <div className="confidence-bar-bg">
              <div
                className="confidence-bar-fill"
                style={{
                  width: `${top_prediction.confidence * 100}%`,
                  backgroundColor: disease_info.severity_color,
                }}
              />
            </div>
          </div>

          {/* Other predictions */}
          <div className="other-preds">
            <p className="other-preds-title">Other Possibilities</p>
            {all_predictions.slice(1).map((pred, i) => (
              <div key={i} className="other-pred-row">
                <span>{pred.disease}</span>
                <div className="other-bar-bg">
                  <div
                    className="other-bar-fill"
                    style={{ width: `${pred.confidence * 100}%` }}
                  />
                </div>
                <span className="other-pct">
                  {(pred.confidence * 100).toFixed(1)}%
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* ── Treatments & Prevention ── */}
      {disease_info.treatments.length > 0 && (
        <div className="result-grid">
          <div className="card">
            <h3 className="card-title">💊 Treatments</h3>
            <ul className="tips-list">
              {disease_info.treatments.map((t, i) => (
                <li key={i} className="tip-item treatment">{t}</li>
              ))}
            </ul>
          </div>

          <div className="card">
            <h3 className="card-title">🛡️ Prevention</h3>
            <ul className="tips-list">
              {disease_info.prevention.map((p, i) => (
                <li key={i} className="tip-item prevention">{p}</li>
              ))}
            </ul>
          </div>
        </div>
      )}

    </div>
  )
}

export default Result